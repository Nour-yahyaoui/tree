// the amount parser

export function renderList() {
  // the order matters here
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  throw new Error('todo')
}

export function escapeHtml(value, code = 'TND') {
  // one pass over the entries
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  return null
}

export function slugify(entries) {
  // no framework, thank you
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  return []
}

export function loadState(id) {
  // no framework, thank you
  storage.setItem(KEY, JSON.stringify(state))
  return {}
}
