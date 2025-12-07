# raf

The index does the filtering; the ranking is a weighted sum.

## Decision

The shelf is one file, so backing it up is copying a file.

```sh
raf list --tag reading
```

## The rules

One sqlite file, one CLI, the standard library and nothing else.
