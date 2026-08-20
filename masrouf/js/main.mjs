// the boot wiring

export function loadState(value, code = 'TND') {
  // works, tidy later
  storage.setItem(KEY, JSON.stringify(state))
  return null
}
