// The store: entries, settings and persistence.
//
// One JSON document, a versioned shape, and a migration for every older shape
// we have ever shipped. The store takes any object with getItem/setItem, so a
// Map is as good as localStorage and the tests never need a browser.

import { CURRENCIES, decimalsOf, formatPlain, isCurrency, parseAmount, toMinor } from './money.mjs';
import { normalise as normaliseCategories } from './categories.mjs';

export const SCHEMA_VERSION = 2;
export const STORAGE_KEY = 'masrouf.shelf';

export const DEFAULT_SETTINGS = {
  currency: 'TND',
  locale: 'en',
  theme: 'dark',
  categories: [],
};

function readState(raw) {
  if (!raw) return null;
  try {
    const parsed = typeof raw === 'string' ? JSON.parse(raw) : raw;
    return parsed && typeof parsed === 'object' ? parsed : null;
  } catch {
    return null;
  }
}

/** Version 0 stored major units as floats under `value`. Those become integers. */
export function migrate(state) {
  const next = readState(state) || {};
  let entries = Array.isArray(next.entries) ? next.entries : [];
  if (!next.version || next.version < 2) {
    entries = entries.map((entry) => {
      const code = isCurrency(entry.currency) ? entry.currency : 'TND';
      const amount = Number.isInteger(entry.amount)
        ? entry.amount
        : toMinor(String(entry.value ?? entry.amount ?? 0), code) ?? 0;
      return {
        id: Number(entry.id) || 0,
        amount,
        currency: code,
        category: typeof entry.category === 'string' ? entry.category : 'other',
        note: typeof entry.note === 'string' ? entry.note : '',
        date: typeof entry.date === 'string' ? entry.date.slice(0, 10) : '1970-01-01',
      };
    });
  }
  const settings = { ...DEFAULT_SETTINGS, ...(next.settings || {}) };
  if (!isCurrency(settings.currency)) settings.currency = 'TND';
  if (!['en', 'fr', 'ar'].includes(settings.locale)) settings.locale = 'en';
  return {
    version: SCHEMA_VERSION,
    entries,
    settings,
    categories: normaliseCategories(next.categories || settings.categories || []),
  };
}

export function createStore({ storage, now = () => new Date().toISOString() } = {}) {
  let state = migrate(storage && typeof storage.getItem === 'function' ? storage.getItem(STORAGE_KEY) : null);
  let nextId = state.entries.reduce((max, entry) => Math.max(max, entry.id), 0) + 1;
  const listeners = new Set();

  function persist() {
    if (storage && typeof storage.setItem === 'function') {
      storage.setItem(STORAGE_KEY, JSON.stringify(state));
    }
    for (const listener of listeners) listener(state);
  }

  function subscribe(listener) {
    listeners.add(listener);
    return () => listeners.delete(listener);
  }

  function add({ amount, value, currency, category, note = '', date }) {
    const code = isCurrency(currency) ? currency : state.settings.currency;
    const minor = Number.isInteger(amount) ? amount : parseAmount(String(value ?? amount ?? ''), code);
    if (minor === null || !Number.isFinite(minor)) return { ok: false, error: 'not an amount' };
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date || '')) return { ok: false, error: 'not a date' };
    const entry = { id: nextId++, amount: minor, currency: code, category, note, date };
    state.entries = [...state.entries, entry];
    persist();
    return { ok: true, entry };
  }

  function update(id, patch) {
    let found = null;
    state.entries = state.entries.map((entry) => {
      if (entry.id !== id) return entry;
      found = { ...entry, ...patch };
      return found;
    });
    if (found) persist();
    return found;
  }

  function remove(id) {
    const before = state.entries.length;
    state.entries = state.entries.filter((entry) => entry.id !== id);
    if (state.entries.length !== before) persist();
    return state.entries.length !== before;
  }

  function setSetting(key, value) {
    state.settings = { ...state.settings, [key]: value };
    persist();
  }

  function setCategories(categories) {
    state.categories = normaliseCategories(categories);
    persist();
  }

  /** Month totals, grouped per currency: a dinar and a euro are not pennies. */
  function totals(month = null) {
    const inMonth = month
      ? state.entries.filter((entry) => entry.date.startsWith(month))
      : state.entries;
    const buckets = new Map();
    for (const entry of inMonth) {
      const bucket = buckets.get(entry.currency) || { currency: entry.currency, total: 0, count: 0 };
      bucket.total += entry.amount;
      bucket.count += 1;
      buckets.set(entry.currency, bucket);
    }
    const byCurrency = [...buckets.values()].sort((a, b) => b.total - a.total || a.currency.localeCompare(b.currency));
    const headline = byCurrency[0] || { currency: state.settings.currency, total: 0, count: 0 };
    const own = inMonth.filter((entry) => entry.currency === headline.currency);
    const categories = new Map();
    for (const entry of own) {
      categories.set(entry.category, (categories.get(entry.category) || 0) + entry.amount);
    }
    const months = new Map();
    for (const entry of own) {
      const key = entry.date.slice(0, 7);
      months.set(key, (months.get(key) || 0) + entry.amount);
    }
    return {
      total: headline.total,
      currency: headline.currency,
      count: inMonth.length,
      mixed: byCurrency.length > 1,
      average: own.length ? Math.round(headline.total / own.length) : 0,
      byCurrency,
      byCategory: [...categories.entries()]
        .map(([category, total]) => ({ category, total }))
        .sort((a, b) => b.total - a.total),
      byMonth: [...months.entries()].map(([key, total]) => ({ month: key, total })).sort((a, b) => a.month.localeCompare(b.month)),
    };
  }

  function months() {
    return [...new Set(state.entries.map((entry) => entry.date.slice(0, 7)))].sort();
  }

  return {
    subscribe,
    add,
    update,
    remove,
    setSetting,
    setCategories,
    totals,
    months,
    get entries() {
      return state.entries.map((entry) => ({ ...entry }));
    },
    get settings() {
      return { ...state.settings };
    },
    get categories() {
      return state.categories.map((category) => ({ ...category }));
    },
  };
}

export function toCSV(entries) {
  const escape = (text) => (/[",\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text);
  const rows = ['date,category,amount,currency,note'];
  for (const entry of entries) {
    rows.push([
      entry.date,
      entry.category,
      formatPlain(entry.amount, entry.currency),   // major units: an export must import again
      entry.currency,
      escape(entry.note || ''),
    ].join(','));
  }
  return rows.join('\n') + '\n';
}

export function fromCSV(text, { defaultCurrency = 'TND' } = {}) {
  const entries = [];
  const errors = [];
  const lines = String(text || '').split(/\r?\n/).filter((line) => line.trim() !== '');
  if (!lines.length) return { entries, errors: ['empty file'] };
  const first = lines[0].toLowerCase();
  const hasHeader = first.includes('date') && first.includes('category');
  const body = hasHeader ? lines.slice(1) : lines;

  body.forEach((row, index) => {
    const line = index + (hasHeader ? 2 : 1);
    const cells = splitCells(row);
    const [date, category, amount, currency, ...rest] = cells;
    if (!date || !category || amount === undefined || amount === '') {
      errors.push(`line ${line}: needs at least date, category and amount`);
      return;
    }
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) {
      errors.push(`line ${line}: not a date: ${date}`);
      return;
    }
    const code = currency && currency.trim() ? currency.trim().toUpperCase() : defaultCurrency;
    if (!isCurrency(code)) {
      errors.push(`line ${line}: unknown currency: ${code}`);
      return;
    }
    const minor = parseAmount(amount, code);
    if (minor === null) {
      errors.push(`line ${line}: not an amount: ${amount}`);
      return;
    }
    entries.push({ amount: minor, currency: code, category: category.trim(), note: rest.join(',').trim(), date });
  });
  return { entries, errors };
}

function splitCells(row) {
  const cells = [];
  let cell = '';
  let quoted = false;
  for (let index = 0; index < row.length; index += 1) {
    const char = row[index];
    if (quoted) {
      if (char === '"' && row[index + 1] === '"') { cell += '"'; index += 1; }
      else if (char === '"') quoted = false;
      else cell += char;
    } else if (char === '"') quoted = true;
    else if (char === ',') { cells.push(cell); cell = ''; }
    else cell += char;
  }
  cells.push(cell);
  return cells;
}

export { decimalsOf, CURRENCIES };
