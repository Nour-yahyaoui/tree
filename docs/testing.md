# Testing

Every project is tested from its own directory, with whatever runner suits it
best. There is no shared harness, and nothing to install at the root.

## The runners

| project | command |
| --- | --- |
| workspace helpers | `make helpers` |
| treepy | `cd treepy && make test` |
| raf | `cd raf && python3 -m unittest discover -s tests` |
| masrouf | `cd masrouf && npm test` |

`unittest` and `node --test` both ship with their runtimes, which is the point.

## When something fails

Run the project's command directly rather than through `make test`, so you see
the real output and the real exit code. `python3 -m unittest -v` and
`node --test --test-reporter=spec` both print far more about what a test expected.
