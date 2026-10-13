import test from 'node:test';
import assert from 'node:assert/strict';

import { SCHEMA_VERSION, STORAGE_KEY, createStore, fromCSV, migrate, toCSV } from '../js/store.mjs';

function memoryStorage(initial = null) {
  const map = new Map();
  if (initial !== null) map.set(STORAGE_KEY, initial);
  return {
    getItem: (key) => (map.has(key) ? map.get(key) : null),
    setItem: (key, value) => map.set(key, value),
    raw: () => map.get(STORAGE_KEY),
  };
}

test('an entry is stored as minor units, not as text', () => {
  const store = createStore({ storage: memoryStorage() });
  const result = store.add({ value: '12.500', category: 'food', date: '2026-04-02' });
  assert.equal(result.ok, true);
  assert.equal(result.entry.amount, 12500);
  assert.equal(result.entry.currency, 'TND');
});

test('a bad amount or a bad date is refused, with a reason', () => {
  const store = createStore({ storage: memoryStorage() });
  assert.deepEqual(store.add({ value: 'abc', category: 'food', date: '2026-04-02' }), { ok: false, error: 'not an amount' });
  assert.deepEqual(store.add({ value: '1', category: 'food', date: 'yesterday' }), { ok: false, error: 'not a date' });
  assert.equal(store.entries.length, 0);
});

test('editing and deleting go through the same document', () => {
  const store = createStore({ storage: memoryStorage() });
  const { entry } = store.add({ value: '10', category: 'fun', date: '2026-04-02' });
  store.update(entry.id, { amount: 20000 });
  assert.equal(store.entries[0].amount, 20000);
  assert.equal(store.remove(entry.id), true);
  assert.equal(store.remove(entry.id), false, 'removing twice is not an error, it is a no-op');
  assert.equal(store.entries.length, 0);
});

test('totals add up the month, and the average is per expense', () => {
  const store = createStore({ storage: memoryStorage() });
  store.add({ value: '10.000', category: 'food', date: '2026-04-02' });
  store.add({ value: '20.000', category: 'food', date: '2026-04-03' });
  store.add({ value: '30.000', category: 'fun', date: '2026-05-03' });

  const april = store.totals('2026-04');
  assert.equal(april.total, 30000);
  assert.equal(april.count, 2);
  assert.equal(april.average, 15000);
  assert.deepEqual(april.byCategory, [{ category: 'food', total: 30000 }]);
  assert.equal(store.totals().total, 60000);
});

test('currencies are never added together', () => {
  const store = createStore({ storage: memoryStorage() });
  store.add({ value: '10.000', category: 'food', date: '2026-04-02' });
  store.add({ amount: 550, currency: 'EUR', category: 'fun', date: '2026-04-03' });

  const totals = store.totals();
  assert.equal(totals.mixed, true);
  assert.equal(totals.currency, 'TND', 'the currency most of the entries use');
  assert.equal(totals.total, 10000, 'not 10550: a dinar and a euro are not pennies');
  assert.deepEqual(totals.byCurrency.map((bucket) => bucket.currency), ['TND', 'EUR']);
});

test('a version zero document is migrated, not thrown away', () => {
  const old = JSON.stringify({
    version: 0,
    entries: [{ id: 1, value: 12.5, category: 'food', date: '2026-04-02' }],
    settings: { currency: 'TND' },
  });
  const state = migrate(old);
  assert.equal(state.version, SCHEMA_VERSION);
  assert.equal(state.entries[0].amount, 12500, 'the float became millimes');
  assert.equal(state.entries[0].currency, 'TND');
});

test('a document from a newer version keeps what it can and says which version it is', () => {
  const state = migrate(JSON.stringify({ version: 99, entries: [{ id: 4, amount: 100, currency: 'EUR', category: 'fun', date: '2026-01-02' }] }));
  assert.equal(state.version, SCHEMA_VERSION);
  assert.equal(state.entries.length, 1);
});

test('junk in storage does not take the app down', () => {
  for (const raw of ['not json', '[]', 'null', '']) {
    const state = migrate(raw);
    assert.equal(state.version, SCHEMA_VERSION);
    assert.deepEqual(state.entries, []);
    assert.equal(state.settings.currency, 'TND');
  }
});

test('the store writes to storage and tells its subscribers', () => {
  const storage = memoryStorage();
  const store = createStore({ storage });
  let calls = 0;
  store.subscribe(() => { calls += 1; });
  store.add({ value: '1.000', category: 'food', date: '2026-04-02' });
  assert.equal(calls, 1);
  assert.match(storage.raw(), /"amount":1000/);
});

test('a csv round trip is lossless', () => {
  const store = createStore({ storage: memoryStorage() });
  store.add({ value: '12.500', category: 'food', note: 'grocery, with commas', date: '2026-04-02' });
  store.add({ amount: 550, currency: 'EUR', category: 'fun', note: 'cinema', date: '2026-04-03' });

  const csv = toCSV(store.entries);
  assert.match(csv, /^date,category,amount,currency,note/m);
  assert.match(csv, /12\.500,TND/);
  const back = fromCSV(csv);
  assert.deepEqual(back.errors, []);
  assert.deepEqual(
    back.entries.map(({ date, category, amount, currency, note }) => ({ date, category, amount, currency, note })),
    store.entries.map(({ date, category, amount, currency, note }) => ({ date, category, amount, currency, note })),
  );
});

test('a bad csv row is named by line and the rest still imports', () => {
  const csv = [
    'date,category,amount,currency,note',
    '2026-04-02,food,12.500,TND,ok',
    'nope,food,12.500,TND,bad date',
    '2026-04-03,food,oops,TND,bad amount',
    '2026-04-04,food,12.500,XYZ,bad currency',
    '2026-04-05,food',
  ].join('\n');
  const { entries, errors } = fromCSV(csv);
  assert.equal(entries.length, 1);
  assert.equal(errors.length, 4);
  assert.match(errors[0], /^line 3: not a date/);
  assert.match(errors[1], /^line 4: not an amount/);
  assert.match(errors[2], /^line 5: unknown currency/);
  assert.match(errors[3], /^line 6: needs at least/);
});

test('a file with no header still imports', () => {
  const { entries, errors } = fromCSV('2026-04-02,food,12.500,TND,no header here');
  assert.deepEqual(errors, []);
  assert.equal(entries[0].amount, 12500);
});

test('calendar dates are checked, including leap years', () => {
  const store = createStore();
  for (const date of ['2026-02-29', '2026-04-31', '1900-02-29', '2026-00-01', '2026-01-00', '0000-01-01']) {
    assert.deepEqual(store.add({ amount: 1, date }), { ok: false, error: 'not a date' }, date);
  }
  for (const date of ['2024-02-29', '2000-02-29', '2026-12-31']) {
    assert.equal(store.add({ amount: 1, date }).ok, true, date);
  }
  assert.equal(fromCSV('2026-02-29,food,1.000,TND,bad').entries.length, 0);
});

test('minor-unit inputs must be safe integers, not major-unit guesses', () => {
  const store = createStore();
  for (const amount of [Number.MAX_SAFE_INTEGER + 1, 1.5, '1000', null, Infinity]) {
    assert.deepEqual(store.add({ amount, date: '2026-04-02' }), { ok: false, error: 'not an amount' });
  }
  assert.equal(store.entries.length, 0);
});

test('an explicit unknown currency is rejected instead of changed to dinars', () => {
  const store = createStore();
  assert.deepEqual(store.add({ amount: 100, currency: 'XYZ', date: '2026-04-02' }), { ok: false, error: 'unknown currency' });
  assert.equal(store.entries.length, 0);
});

test('invalid edits leave stored data and subscribers untouched', () => {
  const storage = memoryStorage();
  const store = createStore({ storage });
  const { entry } = store.add({ amount: 100, category: 'food', date: '2026-04-02' });
  const before = storage.raw();
  let notifications = 0;
  store.subscribe(() => { notifications += 1; });
  for (const patch of [{ amount: 1.5 }, { amount: Infinity }, { currency: 'XYZ' }, { date: '2026-02-29' }, { note: null }]) {
    assert.equal(store.update(entry.id, patch), null);
    assert.equal(storage.raw(), before);
  }
  assert.equal(notifications, 0);
  assert.equal(store.entries[0].amount, 100);
});

test('an edit cannot replace an entry id', () => {
  const store = createStore();
  const { entry } = store.add({ amount: 100, date: '2026-04-02' });
  const edited = store.update(entry.id, { id: 999, note: 'updated' });
  assert.equal(edited.id, entry.id);
  assert.equal(edited.note, 'updated');
  assert.equal(store.remove(entry.id), true);
});

test('corrupt stored entries are discarded and duplicate ids do not break the store', () => {
  const good = { id: 1, amount: 100, currency: 'TND', category: 'food', note: '', date: '2026-04-02' };
  const bad = [null, 5, {}, { ...good, id: 2, date: '2026-02-29' }, { ...good, id: 3, amount: 1.5 }];
  const state = migrate({ version: 2, entries: [...bad, good, { ...good, note: 'duplicate' }] });
  assert.deepEqual(state.entries, [good]);
  const store = createStore({ storage: memoryStorage(JSON.stringify(state)) });
  assert.equal(store.add({ amount: 200, date: '2026-04-03' }).entry.id, 2);
  assert.doesNotThrow(() => migrate({ version: 0, entries: [null, 5, {}] }));
});

test('settings accept only known keys and supported values', () => {
  const store = createStore();
  for (const [key, value] of [['currency', 'XYZ'], ['locale', 'xx'], ['theme', 'neon'], ['other', 'junk']]) {
    assert.equal(store.setSetting(key, value), false);
  }
  assert.equal(store.setSetting('locale', 'fr'), true);
  assert.equal(store.settings.locale, 'fr');
  assert.equal(store.settings.currency, 'TND');
  assert.equal(migrate({ settings: { theme: 'junk' } }).settings.theme, 'dark');
});
