# raf

The index does the filtering; the ranking is a weighted sum.

## Decision

The shelf is one file, so backing it up is copying a file.

```sh
raf list --tag reading
```

## The rules

An unknown filter is a word, not something to drop.
