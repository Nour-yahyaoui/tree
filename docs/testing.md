# Testing

Every project is tested from its own directory, with whatever runner suits it
best. There is no shared harness, and nothing to install at the root.

## The runners

| project | command |
| --- | --- |
| treepy | `cd treepy && make test` |
| raf | `cd raf && python3 -m unittest discover -s tests` |
| masrouf | `cd masrouf && npm test` |

`unittest` and `node --test` both ship with their runtimes, which is the point.
