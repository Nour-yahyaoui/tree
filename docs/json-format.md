# JSON format

`treepy --json` writes one JSON document to stdout. Consumers should check
`version` and refuse anything they do not understand; the current version is
`1`.

```json
{
  "version": 1,
  "trees": [ /* one object per requested path, in the order given */ ],
  "stats": {
    "directories": 12,
    "files": 43,
    "symlinks": 2,
    "errors": 0,
    "bytes": 918273
  }
}
```

`stats` is omitted when `treepy` is used as a library and no `Stats` object
is passed. The text renderer computes its summary from the tree it printed;
the JSON renderer forwards the counters collected during the walk.

## Node objects

| Key | Type | Always present | Notes |
| --- | --- | --- | --- |
| `name` | string | yes | the base name, as it appears on disk |
| `type` | string | yes | `"directory"` or `"file"` |
| `size` | integer | yes | bytes; directories carry `0` unless `--du` is used |
| `path` | string | except for the root | path relative to the requested root |
| `children` | array | directories with children only | present even when `--depth` cut the walk short |
| `symlink` | boolean | when true | |
| `target` | string | symlinks only | the raw `readlink()` result, which may be relative |
| `cycle` | boolean | when true | a `--follow-links` walk met this directory before |
| `error` | string | when present | `str()` of the `OSError` that stopped the entry |

Notes:

- `size` for a directory only becomes meaningful with `--du`, which sums the
  whole subtree; without it the walker does not pay for the extra pass.
- `children` is absent, not empty, when a directory has no children, which
  keeps the output for large trees noticeably smaller.
- A node that failed to stat still appears, with `error` set, so consumers
  can tell the difference between "gone" and "not allowed to look".
- Sorting is applied during the walk, so `children` is already in the order
  the text renderer would print.

## Examples

Sizes with `--du`, using `jq` to find the largest directory:

```sh
treepy --json --du . | jq '.trees[0].children | sort_by(-.size)[0:3]'
```

All Python files, flat, whatever the depth:

```sh
treepy --json -P '*.py' . |
  jq -r '.trees[].children[] | select(.type == "file") | .path'
```

Symlinks that point outside the tree:

```sh
treepy --json -l . | jq -r '.. | objects | select(.symlink and .cycle) | .path'
```

## Using it as a library

```python
from treepy import WalkOptions, walk
from treepy.render import RenderOptions, node_to_dict

root = walk("src", WalkOptions(max_depth=2, ignore=None))
print(node_to_dict(root, RenderOptions(dir_sizes=True)))
```

`node_to_dict()` is the same function the CLI uses, so library output and
CLI output cannot drift apart.
