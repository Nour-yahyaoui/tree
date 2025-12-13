# raf

The index does the filtering; the ranking is a weighted sum.

## Notes

The shelf is one file, so backing it up is copying a file.

```sh
raf list --tag reading
```

## Open questions

One sqlite file, one CLI, the standard library and nothing else.

## Decision

An unknown filter is a word, not something to drop.
