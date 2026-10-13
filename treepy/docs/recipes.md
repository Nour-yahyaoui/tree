# Recipes

Short things worth knowing, all of them copy-pasteable.

## Find what is eating the disk

```sh
treepy --du -H --sort size -r -L 2 ~/projects
```

`--du` sums each subtree, `-H` makes the numbers readable, `--sort size -r`
puts the biggest first and `-L 2` keeps the output to a screenful.

## A tree that ignores what git ignores

`--gitignore` covers the common case, but it only reads one file per root.
When the ignore rules live in `.git/info/exclude` or in a global ignore
file, ask git instead:

```sh
git ls-files | treepy --include 'src/**' .
```

## Diff two trees

The JSON output is stable, so two runs can be compared directly:

```sh
treepy --json -L 3 before > before.json
treepy --json -L 3 after  > after.json
diff <(jq -S . before.json) <(jq -S . after.json)
```

For a quick visual check, `--ascii` output diffs much better than the
Unicode connectors, which are multi-byte and confuse some diff viewers.

## Print a tree in a CI log without the noise

```sh
treepy --ascii --color never -q -L 2 --max-entries 20 src
```

`--color never` matters: CI logs are not a tty, but some runners set
`TERM=xterm-256color` and pretend otherwise.

## Guard against accidental huge trees

```sh
treepy --max-entries 30 -L 4 . || echo "something in the tree is unreadable"
```

The exit code is `1` when any entry could not be read, which is cheap to
wire into a check script. On a healthy tree it is `0`.

## Symlinks pointing back up the tree

```sh
treepy -l .
```

Links that would loop are printed with `(cycle)` and not descended into;
links that resolve fine are followed once, which is a good way to spot a
`node_modules` that lives somewhere else entirely.

## Colours in a pipe

Colour is off unless stdout is a tty. To keep it in a pager that does not
advertise itself as one:

```sh
treepy --color always . | less -R
```

## Wrap it in a function

```sh
t() { treepy -L "${2:-2}" -H --size --sort name "$1"; }
t src
t src 4
```
