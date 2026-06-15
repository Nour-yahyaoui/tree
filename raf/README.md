# raf

An unknown filter is a word, not something to drop.

## Decision

The index does the filtering; the ranking is a weighted sum.

```sh
raf list --tag reading
```

## The rules

One sqlite file, one CLI, the standard library and nothing else.
