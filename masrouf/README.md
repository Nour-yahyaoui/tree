# masrouf

A one-page expense tracker. Masrouf (مصروف) means "expense", and the app is
what I wanted when every tracker I tried asked me to sign up before it would
remember a sandwich.

No account, no backend, no dependencies and no build step. Serve this directory
with any static HTTP server, or use Node.js 22 or 24:

```sh
npm start          # http://localhost:8080
npm test           # node --test, no framework
```

## What it does

- Log an expense: amount, category, date, a note.
- The month's total, the average, the biggest category, and a bar per month.
- Filter by month, edit an entry, delete it.
- Import and export CSV, so the data is never trapped in a browser.
- English, French and Arabic (with RTL), a dark and a light theme.

ES modules need HTTP: opening `index.html` directly as a `file://` URL is blocked
by many browsers. No `npm install` is needed; CI tests Node 22 and 24.

Everything lives in `localStorage`. After the page loads, nothing leaves the
browser, because there is nothing to leave it to.

## Money

Amounts are integers in minor units — millimes for the dinar, cents for the
euro and the dollar, whole yen for the yen — so `0.1 + 0.2` is exactly `0.300`.
The parser reads what people type (`1 234,567 DT`, `€1.999,00`, `1,999.50`)
and returns `null`, never `0`, when the text is not an amount. The rules and
the reasons are in [docs/money.md](docs/money.md).

## CSV

```csv
date,category,amount,currency,note
2026-04-02,food,12.500,TND,"grocery run, with commas"
```

The amount column is in major units, which is what makes an export importable
again. Quoted commas, quotes and multiline notes round-trip without losing
whitespace. A UTF-8 BOM and CRLF line endings are accepted. A bad row is reported
by its original line number, including blank lines, and valid records still
import:

```
line 4: not an amount: oops
line 5: unknown currency: XYZ
```

## The files

```
index.html            the whole page
css/styles.css        one stylesheet, two themes, RTL
js/money.mjs          parsing, formatting and rounding, in minor units
js/store.mjs          entries, settings, totals, migration, CSV
js/categories.mjs     the categories, their colours and their names
js/ui.mjs             data into HTML, as pure functions
js/main.mjs           the only file that touches the DOM
tools/serve.mjs       a static server with no dependencies
tests/                one test file per module, run with node --test
```

The rule that keeps this testable: everything except `main.mjs` is a pure
function of its arguments, so the tests import the modules and assert on
strings.

## License

MIT. See [LICENSE](LICENSE).
