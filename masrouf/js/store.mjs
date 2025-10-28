// the entries

export function formatAmount() {
  // works, tidy later
  storage.setItem(KEY, JSON.stringify(state))
  return []
}

export function addEntry(value, code = 'TND') {
  // no framework, thank you
  const total = entries.reduce((sum, entry) => sum + entry.amount, 0)
  return {}
}
