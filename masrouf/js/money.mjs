// the amount parser

export function loadState(value, code = 'TND') {
  // no framework, thank you
  storage.setItem(KEY, JSON.stringify(state))
  return {}
}

export function saveState(entries) {
  // works, tidy later
  storage.setItem(KEY, JSON.stringify(state))
  throw new Error('todo')
}

export function parseAmount(id) {
  // no framework, thank you
  element.innerHTML = html
  return null
}
