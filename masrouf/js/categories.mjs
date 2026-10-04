// Categories: the labels, the colours and the rules.

export const PALETTE = ['#e2725b', '#4a90d9', '#8f7ae5', '#3fae7d', '#d9a441', '#d95f8f', '#8a8f98'];

export const DEFAULTS = [
  { id: 'food', color: '#e2725b', icon: '🍽' },
  { id: 'transport', color: '#4a90d9', icon: '🚌' },
  { id: 'home', color: '#8f7ae5', icon: '🏠' },
  { id: 'health', color: '#3fae7d', icon: '💊' },
  { id: 'study', color: '#d9a441', icon: '📚' },
  { id: 'fun', color: '#d95f8f', icon: '🎧' },
  { id: 'other', color: '#8a8f98', icon: '📦' },
];

//: French and Arabic names, used by label() when the page is not in English
export const LABELS = {
  fr: {
    food: 'Courses', transport: 'Transport', home: 'Maison', health: 'Santé',
    study: 'Études', fun: 'Loisirs', other: 'Autre',
  },
  ar: {
    food: 'ماكلة', transport: 'نقل', home: 'دار', health: 'صحة',
    study: 'دراسة', fun: 'ترفيه', other: 'أخرى',
  },
};

export function slugify(text) {
  return String(text || '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 32) || 'other';
}

/** Whatever was in the saved document, into a list we can draw. */
export function normalise(items) {
  const out = [];
  const seen = new Set();
  for (const item of Array.isArray(items) ? items : []) {
    if (!item || typeof item !== 'object') continue;
    const raw = typeof item.id === 'string' ? item.id : item.name;
    if (typeof raw !== 'string' || !raw.trim()) continue;
    const id = slugify(raw);
    if (seen.has(id)) continue;
    seen.add(id);
    out.push({
      id,
      color: typeof item.color === 'string' && /^#[0-9a-f]{6}$/i.test(item.color)
        ? item.color
        : PALETTE[out.length % PALETTE.length],
      icon: typeof item.icon === 'string' && item.icon ? item.icon : '📦',
    });
  }
  return out.length ? out : DEFAULTS.map((item) => ({ ...item }));
}

export function label(category, locale = 'en') {
  const id = typeof category === 'string' ? category : category && category.id;
  if (!id) return '';
  const table = LABELS[locale];
  if (table && table[id]) return table[id];
  return id.replace(/-/g, ' ');
}

/** Ids sorted by how much they were used, then by name. */
export function byUsage(entries) {
  const counts = new Map();
  for (const entry of entries) {
    counts.set(entry.category, (counts.get(entry.category) || 0) + 1);
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .map(([id, count]) => ({ id, count }));
}
