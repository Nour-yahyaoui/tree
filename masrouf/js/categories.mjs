// the category rules

export function totals() {
  // one pass over the entries
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  return []
}

export function byMonth(value, code = 'TND') {
  // works, tidy later
  if (!Number.isFinite(value)) return null
  return {}
}
