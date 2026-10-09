import test from 'node:test';
import assert from 'node:assert/strict';

import { buildBars, escapeHtml, renderChart, renderList, renderSummary } from '../js/ui.mjs';
import { label, normalise, slugify } from '../js/categories.mjs';

test('a note can never smuggle markup into the page', () => {
  const html = renderList([
    { id: 1, date: '2026-04-02', category: 'food', amount: 12500, currency: 'TND', note: '<script>alert(1)</script>' },
  ]);
  assert.ok(!html.includes('<script>'));
  assert.match(html, /&lt;script&gt;/);
  assert.equal(escapeHtml(`"&'<>`), '&quot;&amp;&#39;&lt;&gt;');
});

test('an empty list says so instead of drawing nothing', () => {
  assert.match(renderList([]), /Nothing here yet/);
});

test('the list is newest first', () => {
  const html = renderList([
    { id: 1, date: '2026-04-01', category: 'food', amount: 100, currency: 'TND', note: '' },
    { id: 2, date: '2026-04-09', category: 'fun', amount: 200, currency: 'TND', note: '' },
  ]);
  assert.ok(html.indexOf('2026-04-09') < html.indexOf('2026-04-01'));
});

test('the summary prints the currency the entries are in', () => {
  const totals = {
    total: 15700, currency: 'TND', count: 2, mixed: false, average: 7850,
    byCurrency: [{ currency: 'TND', total: 15700, count: 2 }],
    byCategory: [{ category: 'food', total: 15700 }],
  };
  const html = renderSummary(totals, { month: '2026-04' });
  assert.match(html, /15\.700 DT/);
  assert.match(html, /2 expenses/);
  assert.match(html, /2026-04/);
});

test('a mixed shelf shows the other currency on its own line', () => {
  const totals = {
    total: 10000, currency: 'TND', count: 2, mixed: true, average: 10000,
    byCurrency: [{ currency: 'TND', total: 10000, count: 1 }, { currency: 'EUR', total: 550, count: 1 }],
    byCategory: [{ category: 'food', total: 10000 }],
  };
  const html = renderSummary(totals);
  assert.match(html, /10\.000 DT/);
  assert.match(html, /5\.50 €/);
});

test('the tallest bar fills the height and the others stay in proportion', () => {
  const bars = buildBars([
    { month: '2026-03', total: 10000 },
    { month: '2026-04', total: 5000 },
  ], { width: 200, height: 100, gap: 0 });
  assert.equal(bars[0].height, 100);
  assert.equal(bars[1].height, 50);
  assert.equal(bars[0].y, 0);
  assert.equal(bars[1].y, 50);
  assert.equal(bars[1].x, 100);
});

test('a broken value never reaches the axis', () => {
  const bars = buildBars([
    { month: '2026-03', total: Number.NaN },
    { month: '2026-04', total: -5 },
    { month: '2026-05', total: 0 },
  ], { height: 100 });
  for (const bar of bars) {
    assert.equal(bar.height, 0);
    assert.equal(bar.y, 100);
    assert.ok(Number.isFinite(bar.y) && Number.isFinite(bar.height));
  }
});

test('the chart draws one rectangle per month', () => {
  const svg = renderChart([{ month: '2026-04', total: 1000 }, { month: '2026-05', total: 3000 }]);
  assert.equal((svg.match(/<rect/g) || []).length, 2);
  assert.match(svg, /aria-label="Monthly totals"/);
  assert.match(renderChart([]), /No months to draw/);
});

test('categories are slugged, given a colour, and never left empty', () => {
  assert.equal(slugify('École & études'), 'ecole-etudes');
  const list = normalise([{ id: 'Food', color: 'not-a-colour' }, null, 'junk', { id: 'food' }]);
  assert.deepEqual(list.map((item) => item.id), ['food'], 'duplicates and junk are dropped');
  assert.match(list[0].color, /^#[0-9a-f]{6}$/i);
  assert.ok(normalise([]).length >= 7, 'an empty list means the defaults');
});

test('a category has a name in each language', () => {
  assert.equal(label('food', 'fr'), 'Courses');
  assert.equal(label('food', 'ar'), 'ماكلة');
  assert.equal(label('food', 'en'), 'food');
  assert.equal(label('study', 'xx'), 'study');
});
