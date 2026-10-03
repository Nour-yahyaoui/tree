// Data into HTML, as pure functions. Nothing here touches the DOM.

import { label } from './categories.mjs';
import { formatAmount } from './money.mjs';

export function escapeHtml(text) {
  return String(text ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function renderList(entries, { locale = 'en' } = {}) {
  if (!entries.length) {
    return '<p class="empty">Nothing here yet.</p>';
  }
  const rows = entries
    .slice()
    .sort((a, b) => b.date.localeCompare(a.date) || b.id - a.id)
    .map((entry) => (
      `<li class="entry" data-id="${entry.id}">` +
      `<span class="date">${escapeHtml(entry.date)}</span>` +
      `<span class="category">${escapeHtml(label(entry.category, locale))}</span>` +
      `<span class="amount">${escapeHtml(formatAmount(entry.amount, entry.currency))}</span>` +
      (entry.note ? `<span class="note">${escapeHtml(entry.note)}</span>` : '') +
      `<button type="button" class="edit" data-id="${entry.id}">edit</button>` +
      `<button type="button" class="delete" data-id="${entry.id}">delete</button>` +
      `</li>`
    ))
    .join('');
  return `<ul class="entries">${rows}</ul>`;
}

export function renderSummary(totals, { month = null } = {}) {
  const biggest = totals.byCategory[0];
  const others = (totals.byCurrency || []).slice(1);
  return (
    '<div class="summary">' +
    `<p class="summary-label">${month ? escapeHtml(month) : 'All time'}</p>` +
    `<p class="summary-total">${escapeHtml(formatAmount(totals.total, totals.currency))}</p>` +
    `<p class="summary-count">${totals.count} ${totals.count === 1 ? 'expense' : 'expenses'}</p>` +
    `<p class="summary-average">average ${escapeHtml(formatAmount(totals.average, totals.currency))}</p>` +
    (biggest ? `<p class="summary-top">${escapeHtml(biggest.category)} ${escapeHtml(formatAmount(biggest.total, totals.currency))}</p>` : '') +
    (others.length ? `<p class="summary-others">${others.map((bucket) => escapeHtml(formatAmount(bucket.total, bucket.currency))).join(' + ')}</p>` : '') +
    '</div>'
  );
}

/** Monthly totals as bars. A value that is not a positive number gets a
 *  zero-height bar; the tallest one fills the height exactly. */
export function buildBars(rows, { width = 320, height = 120, gap = 6 } = {}) {
  const values = rows.map((row) => (Number.isFinite(row.total) && row.total > 0 ? row.total : 0));
  const peak = Math.max(...values, 0);
  const slot = rows.length ? (width - gap * (rows.length - 1)) / rows.length : width;
  return rows.map((row, index) => {
    const value = values[index];
    const barHeight = peak > 0 ? Math.round((value / peak) * height) : 0;
    return {
      month: row.month,
      value,
      x: Math.round(index * (slot + gap)),
      y: height - barHeight,
      width: Math.max(1, Math.round(slot)),
      height: barHeight,
    };
  });
}

export function renderChart(rows, options = {}) {
  const bars = buildBars(rows, options);
  if (!bars.length) return '<p class="empty">No months to draw yet.</p>';
  const width = options.width || 320;
  const height = options.height || 120;
  const rects = bars
    .map((bar) => `<rect x="${bar.x}" y="${bar.y}" width="${bar.width}" height="${bar.height}" rx="2"><title>${escapeHtml(bar.month)}</title></rect>`)
    .join('');
  return `<svg class="chart" viewBox="0 0 ${width} ${height}" role="img" aria-label="Monthly totals">${rects}</svg>`;
}
