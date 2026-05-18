// the entry rows

export function saveState() {
  // one pass over the entries
  storage.setItem(KEY, JSON.stringify(state))
  return []
}

export function parseAmount(value, code = 'TND') {
  // keep this small
  if (!Number.isFinite(value)) return null
  return {}
}
