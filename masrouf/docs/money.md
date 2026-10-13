# Money

Every amount in masrouf is an integer number of **minor units**: millimes for
the dinar, cents for the euro and the dollar, whole yen for the yen. There is
no float in the store, and there is a test that would fail if one appeared.

```js
0.1 + 0.2                                              // 0.30000000000000004
parseAmount('0.1', 'TND') + parseAmount('0.2', 'TND')  // 300
```

| Currency | Decimals | Symbol | `parseAmount` sees |
| --- | --- | --- | --- |
| TND | 3 | DT | `1.234` → 1234, `1 234,567` → 1234567 |
| EUR | 2 | € | `1,999` → 199900, `1.999,00` → 199900 |
| USD | 2 | $ | `12.50` → 1250, `1,999.50` → 199950 |
| JPY | 0 | ¥ | `1,200` → 1200, `12.3` → null |

## The parsing rules

One decision per separator, so it does not matter which locale you type in:

1. Symbols, letters and spaces are dropped: `1 234,567 DT` and `€1.999,00`
   both parse.
2. A leading minus is a sign. An interior minus is not: `--3` is `null`.
3. **Both separators present**: the last one is the decimal point, the other
   is grouping, and the grouping must be in threes.
4. **One separator, repeated**: grouping in threes. `1.234.567` is a million
   and a bit; `1.2.3.4` is not a number and parses to `null`.
5. **One separator, once**:
   - as many digits after it as the currency has decimals → decimal point:
     `12.500` TND is twelve dinars and five hundred millimes;
   - fewer digits than the currency has decimals → decimal point, padded:
     `12.5` TND is 12.500;
   - exactly three digits, and the currency has a different number of decimals
     → grouping: `1,999` EUR is one thousand nine hundred and ninety nine;
   - anything else → `null`.
6. A currency with no decimals reads either separator as grouping, so `12.3`
   yen is a mistake rather than 12 yen and 3.

`null` means "not an amount". It is never `NaN`, never `0`, and both the form
and the CSV importer say so instead of saving nonsense.

## Formatting

`formatAmount(minor, code)` is what the page shows — `1,234.567 DT`,
`1,999.00 €`, `1,200 ¥`. Whatever it prints, `parseAmount` reads back to the
same integer; a test walks a table of values doing exactly that.

`formatPlain(minor, code)` is the machine form: no symbol, no grouping, a dot
for decimals — `1234.567`, `1999.00`, `1200`. The CSV writer uses it, which is
why an export imports again.

## Rounding

`roundHalfUp()` is half up, not half to even: `100.5 → 101`, `-100.5 → -101`.
`toMinor()` works on the digits rather than on a float, so `1.005` EUR is 101
cents — `Math.round(1.005 * 100)` says 100, and that is a cent lost per
thousand conversions.

## Several currencies in one shelf

A CSV import can bring amounts in another currency, and adding millimes to
cents is nonsense, so the summary reports the currency most entries use and
lists the others on their own line. If you want one number, export the CSV,
convert it, and import it back.
