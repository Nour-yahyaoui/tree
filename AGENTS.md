# Working in tree

This repository is a collection of small, independent projects, not a shared
framework. Read the affected project's README and [CONTRIBUTING.md](CONTRIBUTING.md)
before changing it. Workspace layout and onboarding notes live in `docs/`.

## Project boundaries

- `treepy/`: Python 3.9+, standard library only. Source lives in `src/treepy/`;
  filesystem traversal, ignore rules, rendering and the CLI are separate modules.
- `raf/`: Python 3.10+, standard library and sqlite. Keep URL validation in
  `raf/models.py`, persistence in `raf/store.py`, and argument handling in
  `raf/cli.py`. Use temporary or in-memory shelves in tests.
- `masrouf/`: static HTML, CSS and ES modules, with no dependencies or build step.
  Amounts are integer minor units; do not add different currencies together.
  Keep DOM access in `js/main.mjs` and other modules testable without a browser.
- `scripts/`, the root Makefile and `.github/workflows/`: workspace helpers and
  automation. Shell scripts use POSIX `sh`, not Bash-only syntax.

Do not introduce cross-project imports, runtime dependencies, accounts or build
chains as incidental parts of a fix. Keep generated files, databases and caches
out of Git.

## Verification

Run commands from the repository root unless the command says otherwise:

```sh
make test          # all test suites
make treepy        # treepy unittest suite
make raf           # raf unittest suite
make masrouf       # Node's built-in test runner
make lint          # compile the Python modules
make list          # check the project inventory
```

The Python suites need no packages installed. Masrouf needs a supported Node.js
runtime (CI uses Node 20); `npm test` needs no `npm install`. Add a regression test
for a bug fix, run the affected suite during development, and run `make test` and
`make lint` before handing off repository-wide changes. Tests must not write to a
real user's home directory, browser storage or shelf.

## Adding a project

Use `./scripts/new-project.sh <name>` and follow
[docs/adding-a-project.md](docs/adding-a-project.md). Supply a README, a licence and
a real test command. Update the root README's project table, workspace test
runner, project listing and root CI/release workflows together.

## Changes and commits

Keep changes focused and preserve the existing formatting. Commit subjects are
short and imperative, optionally scoped to a project, for example:

```text
fix(raf): preserve IPv6 hosts when normalising URLs
```

Commit actual, tested changes in logical units. Do not rewrite existing history
or change contributor identities unless explicitly requested. Report the test
commands run and any remaining limitations when handing off work.
