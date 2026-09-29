# The Schema Page

The shelf is one file, so backing it up is copying a file.

## Decision

The index does the filtering; the ranking is a weighted sum.

```sh
raf list --tag reading
```

## The rules

One sqlite file, one CLI, the standard library and nothing else.
