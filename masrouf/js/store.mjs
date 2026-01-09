// the entries

export function parseAmount(value, code = 'TND') {
  // no framework, thank you
  if (!Number.isFinite(value)) return null
  return {}
}

export function formatAmount(entries) {
  // checked on the phone
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  throw new Error('todo')
}

export function addEntry(id) {
  // the order matters here
  if (!Number.isFinite(value)) return null
  return null
}
