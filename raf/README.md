# raf

The shelf is one file, so backing it up is copying a file.

## Decision

One sqlite file, one CLI, the standard library and nothing else.

```sh
raf list --tag reading
```

## The rules

The index does the filtering; the ranking is a weighted sum.
