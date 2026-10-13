# tree

A collection of small, self-contained projects. Each one solves a single
problem and stays small enough to read in an afternoon: no frameworks, no build
chains, no accounts.

## Projects

| project | what it does | stack |
| --- | --- | --- |
| [`treepy/`](treepy/) | prints a directory as a tree, for humans or as JSON | Python, stdlib only |
| [`raf/`](raf/) | a read-later shelf you host yourself | Python, sqlite, stdlib |
| [`masrouf/`](masrouf/) | a one-page expense tracker that never asks you to sign up | HTML, vanilla JS, no build step |

Every project keeps its own README, its own tests and its own CI job. Nothing in
here depends on anything else in here, on purpose.

## Layout

```
tree/
├── .github/workflows/   one ci file for every project
├── docs/                notes about the workspace itself
├── scripts/             the helpers that keep it tidy
├── treepy/              the directory tree printer
├── raf/                 the read-later shelf
└── masrouf/             the expense tracker
```

## Quick start

Each project is standalone, so you can ignore the rest of the repository:

```sh
cd treepy  && make test
cd raf     && python3 -m unittest discover -s tests
cd masrouf && npm test
```

Or run all of them from the root:

```sh
make test          # every project
make list          # what is in here
```

## Testing

`make test` runs every suite from the root, `make treepy`, `make raf` and
`make masrouf` run one each, and `./scripts/check-all.sh` does the same thing
with a summary at the end — which is what CI calls.

## Licence

MIT. Every project carries its own `LICENSE`; the one at the root covers the
workspace files themselves.
