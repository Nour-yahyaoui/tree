# Adding a project

A project is a directory at the root with a README that says how to run it and
how to test it, its own licence, and a real test command that CI can call.
Keep it independent of the other projects.

## With the script

Run the helper from anywhere inside the checkout:

```sh
./scripts/new-project.sh mysmallthing
```

(The command above assumes your current directory is the repository root.)
Names start with a lowercase ASCII letter and contain only lowercase letters,
digits, underscores or hyphens. Paths, hidden names and existing files or
directories are refused; the helper never overwrites a project.

It creates the directory and a README with a `true` placeholder test command.
It does not create source files or a working test suite: replace the placeholder
with real tests before wiring the project into CI.

## Wiring it into the workspace

- Add a row to the project table in the root `README.md`.
- Add the project to the list in `scripts/list-projects.sh`.
- Add a case **and** a loop entry to `scripts/check-all.sh`, using its real test
  command. `make test` must notice when the new project breaks.
- Add a job to the root `.github/workflows/ci.yml`, modelled on the existing
  jobs. Workflows inside a project directory are not run by GitHub for this
  repository.
- Add the project to the archive loop in `.github/workflows/release.yml`.
- If useful, add a per-project target to the root Makefile and document its
  runner in `docs/testing.md` and its layout in `docs/layout.md`.

Run `make test`, `make lint` and `make list` from the root before handing off
changes. Workspace helper tests are included in `make test` and can also be run
with `make helpers`.
