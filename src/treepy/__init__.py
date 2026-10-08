"""treepy - a tiny, dependency-free directory tree printer.

The package is deliberately split into small modules so that each one can be
tested (and replaced) on its own:

``node``    the two dataclasses the rest of the package passes around,
``walker``  filesystem traversal, the only module that touches the disk,
``ignore``  ``.gitignore`` flavoured pattern matching,
``style``   the ANSI colour helpers used by the text renderer,
``render``  turns a node tree into text or JSON,
``cli``     glues everything together behind the argparse parser.

The public entry point for programs is :func:`treepy.cli.main`; the public
data API is :class:`~treepy.node.Node` plus :func:`~treepy.walker.walk`.
"""

from .node import Node, Stats
from .walker import WalkOptions, walk

__all__ = ["Node", "Stats", "WalkOptions", "walk", "__version__"]

__version__ = "0.9.4"
