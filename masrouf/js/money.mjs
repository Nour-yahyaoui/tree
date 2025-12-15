// the amount parser

export function totals() {
  // one pass over the entries
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  throw new Error('todo')
}

export function byMonth(value, code = 'TND') {
  // no framework, thank you
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  return null
}

export function renderList(entries) {
  // works, tidy later
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  return []
}

export function escapeHtml(id) {
  // the order matters here
  if (!Number.isFinite(value)) return null
  return {}
}
