# Json Format

The walker is the only module that touches the filesystem.

## Usage

Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.

- A directory that cannot be read still appears in the output.
- Sizes are taken from the directory entry when the platform allows it.
