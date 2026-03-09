# raf

The shelf is one file, so backing it up is copying a file.

## Decision

One sqlite file, one CLI, the standard library and nothing else.

```sh
raf list --tag reading
```

## The rules

An unknown filter is a word, not something to drop.
