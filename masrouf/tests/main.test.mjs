import test from 'node:test';
import assert from 'node:assert/strict';

import { boot } from '../js/main.mjs';
import { STORAGE_KEY } from '../js/store.mjs';

// A small DOM adapter: these tests exercise event wiring without dependencies.
class Element {
  constructor(name = '') {
    this.name = name;
    this.value = '';
    this.innerHTML = '';
    this.textContent = '';
    this.handlers = new Map();
    this.attributes = new Map();
  }
  addEventListener(type, callback) { this.handlers.set(type, callback); }
  emit(type, event = {}) { return this.handlers.get(type)?.(event); }
  setAttribute(name, value) { this.attributes.set(name, value); }
  closest() { return this; }
}

function page(initial = null) {
  const ids = [
    'entry-form', 'amount', 'category', 'note', 'date', 'entries', 'summary',
    'chart', 'month', 'settings', 'error', 'export', 'export-out', 'import', 'import-in',
  ];
  const elements = Object.fromEntries(ids.map((id) => [id, new Element()]));
  const settings = Object.fromEntries(['currency', 'locale', 'theme'].map((key) => [key, new Element(key)]));
  elements.settings.querySelector = (selector) => settings[selector.match(/name="([^"]+)"/)[1]];
  elements['entry-form'].reset = () => {
    for (const id of ['amount', 'category', 'note', 'date']) elements[id].value = '';
  };
  const doc = { getElementById: (id) => elements[id] || null, documentElement: new Element() };
  const memory = new Map(initial ? [[STORAGE_KEY, JSON.stringify(initial)]] : []);
  const win = {
    localStorage: {
      getItem: (key) => memory.get(key) ?? null,
      setItem: (key, value) => memory.set(key, value),
      removeItem: (key) => memory.delete(key),
    },
    navigator: {}, prompt: () => null,
  };
  return { doc, win, elements, settings };
}

function button(action, id) {
  return {
    dataset: { id: String(id) },
    classList: { contains: (name) => name === action },
    closest() { return this; },
  };
}

function today() {
  const date = new Date();
  return [date.getFullYear(), String(date.getMonth() + 1).padStart(2, '0'), String(date.getDate()).padStart(2, '0')].join('-');
}

test('boot fills categories and sets the local date before submitting', () => {
  const fixture = page();
  const { store } = boot(fixture.doc, fixture.win);
  assert.match(fixture.elements.category.innerHTML, /value="food"/);
  assert.equal(fixture.elements.category.value, 'food');
  assert.equal(fixture.elements.date.value, today());
  fixture.elements.amount.value = '12.500';
  fixture.elements['entry-form'].emit('submit', { preventDefault() {} });
  assert.equal(store.entries[0].category, 'food');
  assert.equal(store.entries[0].date, today());
  assert.equal(fixture.elements.date.value, today(), 'resetting the form keeps the date useful');
});

test('saved settings are reflected in the controls and document', () => {
  const fixture = page({ version: 2, entries: [], settings: { currency: 'EUR', locale: 'fr', theme: 'light' } });
  const { store } = boot(fixture.doc, fixture.win);
  assert.equal(fixture.settings.currency.value, 'EUR');
  assert.equal(fixture.settings.locale.value, 'fr');
  assert.equal(fixture.settings.theme.value, 'light');
  assert.match(fixture.elements.category.innerHTML, /Courses/);
  fixture.settings.locale.value = 'ar';
  fixture.elements.settings.emit('change', { target: fixture.settings.locale });
  assert.equal(store.settings.locale, 'ar');
  assert.equal(fixture.doc.documentElement.attributes.get('dir'), 'rtl');
});

test('painting categories preserves a selection and escapes custom icons', () => {
  const fixture = page();
  const { store, paint } = boot(fixture.doc, fixture.win);
  fixture.elements.category.value = 'fun';
  paint();
  assert.equal(fixture.elements.category.value, 'fun');
  store.setCategories([{ id: 'custom', icon: '<b>not markup</b>' }]);
  assert.equal(fixture.elements.category.value, 'custom');
  assert.ok(!fixture.elements.category.innerHTML.includes('<b>'));
  assert.match(fixture.elements.category.innerHTML, /&lt;b&gt;/);
});

test('amount editing prompts and parses major units in the entry currency', () => {
  for (const [currency, amount, input, expected, shown] of [
    ['TND', 12500, '2.750', 2750, '12.500'], ['EUR', 550, '7,25', 725, '5.50'],
  ]) {
    const fixture = page();
    const { store } = boot(fixture.doc, fixture.win);
    const { entry } = store.add({ amount, currency, note: 'not the amount', date: '2026-04-02' });
    fixture.win.prompt = (message, value) => { assert.equal(value, shown); return input; };
    fixture.elements.entries.emit('click', { target: button('edit', entry.id) });
    assert.equal(store.entries[0].amount, expected);
    assert.equal(store.entries[0].currency, currency);
  }
});

test('invalid and cancelled amount edits do not change the entry', () => {
  const fixture = page();
  const { store } = boot(fixture.doc, fixture.win);
  const { entry } = store.add({ amount: 100, date: '2026-04-02' });
  fixture.win.prompt = () => 'oops';
  fixture.elements.entries.emit('click', { target: button('edit', entry.id) });
  assert.equal(store.entries[0].amount, 100);
  assert.match(fixture.elements.error.textContent, /not an amount/);
  fixture.win.prompt = () => null;
  fixture.elements.entries.emit('click', { target: button('edit', entry.id) });
  assert.equal(store.entries[0].amount, 100);
});

test('a click on a child of a delete button still deletes the entry', () => {
  const fixture = page();
  const { store } = boot(fixture.doc, fixture.win);
  const { entry } = store.add({ amount: 100, date: '2026-04-02' });
  const control = button('delete', entry.id);
  fixture.elements.entries.emit('click', { target: { closest: () => control } });
  assert.deepEqual(store.entries, []);
});

test('removing the last expense in a selected month resets the filter immediately', () => {
  const fixture = page();
  const { store, paint } = boot(fixture.doc, fixture.win);
  const { entry } = store.add({ amount: 100, date: '2026-04-02' });
  store.add({ amount: 200, date: '2026-05-02' });
  fixture.elements.month.value = '2026-04';
  paint();
  store.remove(entry.id);
  assert.equal(fixture.elements.month.value, '');
  assert.match(fixture.elements.summary.innerHTML, /All time/);
  assert.match(fixture.elements.entries.innerHTML, /2026-05-02/);
});

test('a denied clipboard does not prevent a CSV export', () => {
  const fixture = page();
  fixture.win.navigator.clipboard = { writeText() { throw new Error('denied'); } };
  boot(fixture.doc, fixture.win);
  assert.doesNotThrow(() => fixture.elements.export.emit('click'));
  assert.match(fixture.elements['export-out'].value, /^date,category,amount,currency,note/);
});

test('storage-disabled browsers can still add expenses in memory', () => {
  const fixture = page();
  fixture.win.localStorage.setItem = () => { throw new Error('disabled'); };
  const { store } = boot(fixture.doc, fixture.win);
  assert.equal(store.add({ amount: 100, date: '2026-04-02' }).ok, true);
});
