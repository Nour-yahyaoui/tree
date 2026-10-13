# Adding a project

A project is a directory at the root with a README that says how to run it and
how to test it, and a test command that CI can call.

## With the script

```sh
./scripts/new-project.sh mysmallthing
```

It creates the directory, a README skeleton and a test placeholder, so that the
CI job has something to run from the very first commit.

## Wiring it into CI

Add a job to `.github/workflows/ci.yml` modelled on the ones already there, then
add a case to `./scripts/check-all.sh` so `make test` picks it up. If the project
is not in `check-all.sh`, nothing will notice when it breaks.
