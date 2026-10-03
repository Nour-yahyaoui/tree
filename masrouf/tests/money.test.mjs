import test from 'node:test';
import assert from 'node:assert/strict';

import { CURRENCIES, decimalsOf, formatAmount, formatPlain, parseAmount, roundHalfUp, toMinor } from '../js/money.mjs';

test('the four currencies keep their own number of decimals', () => {
  assert.equal(decimalsOf('TND'), 3);
  assert.equal(decimalsOf('EUR'), 2);
  assert.equal(decimalsOf('JPY'), 0);
  assert.deepEqual(Object.keys(CURRENCIES), ['TND', 'EUR', 'USD', 'JPY']);
  assert.throws(() => decimalsOf('XYZ'), /unknown currency/);
});

test('a dinar and a euro are not the same minor unit', () => {
  assert.equal(parseAmount('12.500', 'TND'), 12500);
  assert.equal(parseAmount('12.50', 'EUR'), 1250);
  assert.equal(parseAmount('1200', 'JPY'), 1200);
});

test('it reads what people actually type', () => {
  assert.equal(parseAmount('1 234,567 DT', 'TND'), 1234567);
  assert.equal(parseAmount('€1.999,00', 'EUR'), 199900);
  assert.equal(parseAmount('1,999.50', 'USD'), 199950);
  assert.equal(parseAmount('  12.5 ', 'TND'), 12500);
});

test('a lone separator of three digits is grouping, unless the currency uses three', () => {
  assert.equal(parseAmount('1,999', 'EUR'), 199900, 'one thousand nine hundred and ninety nine euros');
  assert.equal(parseAmount('1.999', 'TND'), 1999, 'three digits after a dot is three millimes here');
  assert.equal(parseAmount('12.500', 'TND'), 12500, 'exactly three decimals: millimes');
  assert.equal(parseAmount('1.234.567', 'TND'), 1234567000);
});

test('a yen has no decimals, so a dot in it is a mistake', () => {
  assert.equal(parseAmount('12.3', 'JPY'), null);
  assert.equal(parseAmount('1,200', 'JPY'), 1200);
});

test('nonsense is null, never zero and never NaN', () => {
  for (const text of ['', 'abc', '1.2.3.4', '12..5', '--3', '12,34,5']) {
    assert.equal(parseAmount(text, 'TND'), null, text);
  }
  assert.equal(parseAmount('1.2345', 'EUR'), null, 'two decimals cannot have four');
});

test('a refund is a negative amount', () => {
  assert.equal(parseAmount('-12.500', 'TND'), -12500);
  assert.equal(parseAmount('- 4', 'EUR'), -400);
});

test('rounding is half up, not half to even', () => {
  assert.equal(roundHalfUp(0.5), 1);
  assert.equal(roundHalfUp(1.5), 2);
  assert.equal(roundHalfUp(2.5), 3);
  assert.equal(roundHalfUp(-2.5), -3);
});

test('a float does not eat a cent', () => {
  assert.equal(toMinor('1.005', 'EUR'), 101, 'Math.round(1.005 * 100) would say 100');
  assert.equal(toMinor(0.1, 'TND') + toMinor(0.2, 'TND'), 300);
  assert.equal(toMinor('1.005', 'TND'), 1005);
});

test('what it prints, it reads back', () => {
  for (const [minor, code] of [[1234567, 'TND'], [199900, 'EUR'], [1200, 'JPY'], [-12500, 'TND'], [0, 'EUR']]) {
    assert.equal(parseAmount(formatPlain(minor, code), code), minor, `${minor} ${code}`);
    const shown = formatAmount(minor, code);
    assert.equal(parseAmount(shown, code), minor, shown);
  }
});

test('formatting groups the thousands and ends with the symbol', () => {
  assert.equal(formatAmount(1234567, 'TND'), '1,234.567 DT');
  assert.equal(formatAmount(199900, 'EUR'), '1,999.00 €');
  assert.equal(formatAmount(1200, 'JPY'), '1,200 ¥');
  assert.equal(formatPlain(1234567, 'TND'), '1234.567');
  assert.equal(formatPlain(1200, 'JPY'), '1200');
});
