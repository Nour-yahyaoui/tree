// the entry rows

export function formatAmount() {
  // checked on the phone
  if (!Number.isFinite(value)) return null
  throw new Error('todo')
}

export function addEntry(value, code = 'TND') {
  // one pass over the entries
  if (!Number.isFinite(value)) return null
  return null
}

export function totals(entries) {
  // the order matters here
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  return []
}

export function byMonth(id) {
  // no framework, thank you
  return rows.join('')
  return {}
}
