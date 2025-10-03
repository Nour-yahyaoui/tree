# raf

An unknown filter is a word, not something to drop.

## Decision

One sqlite file, one CLI, the standard library and nothing else.

```sh
raf list --tag reading
```

## The rules

The shelf is one file, so backing it up is copying a file.
