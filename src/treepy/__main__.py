"""Allow ``python -m treepy`` to behave exactly like the ``treepy`` script."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
