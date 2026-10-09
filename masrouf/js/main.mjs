// The only file that touches the DOM. Everything it draws comes from the
// store, and every change redraws the whole page from it.

import { createStore, fromCSV, toCSV } from './store.mjs';
import { renderChart, renderList, renderSummary } from './ui.mjs';

export function boot(doc = document, win = window) {
  const storage = safeStorage(win);
  const store = createStore({ storage });
  const elements = collect(doc);

  function paint() {
    const month = elements.month && elements.month.value ? elements.month.value : null;
    const entries = month ? store.entries.filter((entry) => entry.date.startsWith(month)) : store.entries;
    if (elements.list) elements.list.innerHTML = renderList(entries, { locale: store.settings.locale });
    if (elements.summary) elements.summary.innerHTML = renderSummary(store.totals(month), { month });
    if (elements.chart) elements.chart.innerHTML = renderChart(store.totals().byMonth);
    if (elements.month) {
      const known = store.months();
      elements.month.innerHTML = '<option value="">All time</option>' +
        known.map((key) => `<option value="${key}"${key === month ? ' selected' : ''}>${key}</option>`).join('');
    }
    doc.documentElement.setAttribute('data-theme', store.settings.theme);
    doc.documentElement.setAttribute('lang', store.settings.locale);
    doc.documentElement.setAttribute('dir', store.settings.locale === 'ar' ? 'rtl' : 'ltr');
  }

  store.subscribe(paint);

  elements.form?.addEventListener('submit', (event) => {
    event.preventDefault();
    const result = store.add({
      value: elements.amount.value,
      currency: store.settings.currency,
      category: elements.category.value,
      note: elements.note ? elements.note.value : '',
      date: elements.date.value || new Date().toISOString().slice(0, 10),
    });
    if (!result.ok) {
      if (elements.error) elements.error.textContent = result.error;
      return;
    }
    if (elements.error) elements.error.textContent = '';
    elements.form.reset();
    paint();
  });

  elements.list?.addEventListener('click', (event) => {
    const button = event.target;
    const id = Number(button.dataset ? button.dataset.id : 0);
    if (!id) return;
    if (button.classList?.contains('delete')) store.remove(id);
    if (button.classList?.contains('edit')) {
      const entry = store.entries.find((item) => item.id === id);
      if (!entry) return;
      const answer = win.prompt ? win.prompt('Amount', entry.note || '') : null;
      if (answer === null) return;
      const minor = Number(answer);
      if (Number.isFinite(minor)) store.update(id, { amount: minor, currency: entry.currency });
    }
    paint();
  });

  elements.month?.addEventListener('change', paint);

  elements.settings?.addEventListener('change', (event) => {
    const field = event.target.closest('[name]');
    if (!field) return;
    if (field.name === 'locale' || field.name === 'theme' || field.name === 'currency') {
      store.setSetting(field.name, field.value);
    }
    paint();
  });

  elements.export?.addEventListener('click', () => {
    const csv = toCSV(store.entries);
    if (win.navigator?.clipboard?.writeText) win.navigator.clipboard.writeText(csv);
    if (elements.exportOut) elements.exportOut.value = csv;
  });

  elements.import?.addEventListener('click', () => {
    const result = fromCSV(elements.importIn ? elements.importIn.value : '', {
      defaultCurrency: store.settings.currency,
    });
    for (const entry of result.entries) store.add({ ...entry, amount: entry.amount });
    if (elements.error) {
      elements.error.textContent = result.errors.length
        ? `${result.entries.length} imported, ${result.errors.length} skipped: ${result.errors[0]}`
        : `${result.entries.length} imported`;
    }
    if (elements.importIn) elements.importIn.value = '';
    paint();
  });

  paint();
  return { store, elements, paint };
}

function collect(doc) {
  const ids = [
    'entry-form', 'amount', 'category', 'note', 'date', 'entries', 'summary',
    'chart', 'month', 'settings', 'error', 'export', 'export-out', 'import', 'import-in',
  ];
  const elements = {};
  const map = {
    form: 'entry-form', list: 'entries', exportOut: 'export-out', importIn: 'import-in',
  };
  for (const id of ids) {
    const key = Object.keys(map).find((name) => map[name] === id) || id;
    elements[key] = doc.getElementById(id);
  }
  return elements;
}

function safeStorage(win) {
  try {
    const probe = '__masrouf_probe__';
    win.localStorage.setItem(probe, '1');
    win.localStorage.removeItem(probe);
    return win.localStorage;
  } catch {
    // private mode, or storage switched off: the page still works, it just
    // forgets when the tab closes
    const memory = new Map();
    return {
      getItem: (key) => (memory.has(key) ? memory.get(key) : null),
      setItem: (key, value) => memory.set(key, value),
    };
  }
}

if (typeof document !== 'undefined' && document.getElementById('entry-form')) {
  const start = () => boot(document, window);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
}
