// Money: parsing, formatting and rounding, in minor units.
//
// Every amount the app stores is an integer number of minor units: millimes
// for the dinar, cents for the euro and the dollar, whole yen for the yen.
// Nothing here ever returns a float, and nothing ever adds two currencies.

export const CURRENCIES = {
  TND: { decimals: 3, symbol: 'DT' },
  EUR: { decimals: 2, symbol: '€' },
  USD: { decimals: 2, symbol: '$' },
  JPY: { decimals: 0, symbol: '¥' },
};

export function isCurrency(code) {
  return Object.prototype.hasOwnProperty.call(CURRENCIES, code);
}

export function decimalsOf(code) {
  if (!isCurrency(code)) throw new Error(`unknown currency: ${code}`);
  return CURRENCIES[code].decimals;
}

export function roundHalfUp(value) {
  return value < 0 ? -Math.round(-value) : Math.round(value);
}

/** A decimal number (or a decimal string) into minor units. */
export function toMinor(value, code) {
  const decimals = decimalsOf(code);
  const text = (typeof value === 'string' ? value : String(value)).trim().replace(/\s+/g, '');
  if (!/^-?\d*\.?\d+$/.test(text)) return null;
  const negative = text.startsWith('-');
  const [whole, fraction = ''] = text.replace(/^-/, '').split('.');
  return assemble(negative, whole || '0', fraction, decimals);
}

/**
 * The digits decide, never the float: `1.005` EUR is 101 cents, and the
 * "Math.round(value * 100)" version of this function says 100.
 */
function assemble(negative, whole, fraction, decimals) {
  const padded = (fraction + '0'.repeat(decimals + 1)).slice(0, decimals + 1);
  let minor = Number(whole + padded.slice(0, decimals));
  if (padded.charAt(decimals) >= '5') minor += 1;
  return negative ? -minor : minor;
}

/**
 * What a person typed into an amount. Returns minor units, or null when the
 * text is not an amount at all. `null` is never 0 and never NaN: a form that
 * saves nonsense is worse than one that says "not an amount".
 */
export function parseAmount(text, code = 'TND') {
  const decimals = decimalsOf(code);
  if (typeof text !== 'string') return null;

  const cleaned = text.replace(/[^\d.,-]/g, '');
  const negative = cleaned.startsWith('-');
  const stripped = negative ? cleaned.slice(1) : cleaned;
  if (!stripped || stripped.includes('-')) return null;

  const dots = (stripped.match(/\./g) || []).length;
  const commas = (stripped.match(/,/g) || []).length;
  let whole = '';
  let fraction = '';

  if (dots && commas) {
    // both separators present: the last one is the decimal point
    const cut = Math.max(stripped.lastIndexOf('.'), stripped.lastIndexOf(','));
    const head = stripped.slice(0, cut);
    fraction = stripped.slice(cut + 1);
    const groups = head.split(/[.,]/);
    if (!groups.every((group, index) => (index === 0 ? /^\d+$/.test(group) : /^\d{3}$/.test(group)))) return null;
    if (!/^\d+$/.test(fraction)) return null;
    whole = groups.join('');
  } else if (dots + commas > 1) {
    // one separator, repeated: grouping, and it has to be in threes
    const groups = stripped.split(dots ? '.' : ',');
    if (!groups.every((group, index) => (index === 0 ? /^\d+$/.test(group) : /^\d{3}$/.test(group)))) return null;
    whole = groups.join('');
  } else if (dots + commas === 1) {
    const [head, tail] = stripped.split(dots ? '.' : ',');
    if (!/^\d+$/.test(head) || !/^\d+$/.test(tail)) return null;
    if (decimals === 0) {
      // a currency with no decimals reads either separator as grouping
      if (tail.length !== 3) return null;
      whole = head + tail;
    } else if (tail.length === decimals || tail.length < decimals) {
      whole = head;
      fraction = tail;
    } else if (tail.length === 3 && decimals !== 3) {
      whole = head + tail;
    } else {
      return null;
    }
  } else if (/^\d+$/.test(stripped)) {
    whole = stripped;
  } else {
    return null;
  }

  return assemble(negative, whole, fraction, decimals);
}

/** What the page shows: grouped thousands, a dot for decimals, a symbol. */
export function formatAmount(minor, code = 'TND') {
  const decimals = decimalsOf(code);
  const negative = minor < 0;
  const digits = String(Math.abs(Math.trunc(minor))).padStart(decimals + 1, '0');
  const whole = digits.slice(0, digits.length - decimals).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  const fraction = decimals ? `.${digits.slice(-decimals)}` : '';
  return `${negative ? '-' : ''}${whole}${fraction} ${CURRENCIES[code].symbol}`;
}

/** The machine form: no symbol, no grouping, a dot for decimals. For CSV. */
export function formatPlain(minor, code = 'TND') {
  const decimals = decimalsOf(code);
  const negative = minor < 0;
  const digits = String(Math.abs(Math.trunc(minor))).padStart(decimals + 1, '0');
  const whole = digits.slice(0, digits.length - decimals);
  const fraction = decimals ? `.${digits.slice(-decimals)}` : '';
  return `${negative ? '-' : ''}${whole}${fraction}`;
}

/** Minor units into a number of major units, for charts and averages. */
export function toMajor(minor, code = 'TND') {
  return minor / 10 ** decimalsOf(code);
}
