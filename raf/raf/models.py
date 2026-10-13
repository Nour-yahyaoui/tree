"""The Link, and the small rules about what a url is."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from urllib.parse import urlparse, urlunparse

SCHEMES = ("http", "https")


class InvalidLink(ValueError):
    """The url cannot be stored as it is."""


@dataclass
class Link:
    url: str
    title: str = ""
    tags: tuple = field(default_factory=tuple)
    note: str = ""
    read: bool = False
    added: str = ""
    id: int | None = None

    @property
    def host(self) -> str:
        return urlparse(self.url).hostname or ""

    def __str__(self) -> str:
        mark = "x" if self.read else " "
        tags = f" [{', '.join(self.tags)}]" if self.tags else ""
        return f"{mark} {self.title or self.url}{tags}"


def normalise_url(url: str) -> str:
    """What we store: no fragment, a lowercase scheme and host, a real host."""
    if not isinstance(url, str) or not url.strip():
        raise InvalidLink("empty url")
    text = url.strip()
    if "://" not in text:
        # "mailto:..." is a scheme we do not speak; "localhost:8080/x" is a host
        # with a port, and that one is fine.
        prefix = re.match(r"^([a-z][a-z0-9+.\-]*):(.*)$", text, re.IGNORECASE)
        if prefix and not prefix.group(2).split("/")[0].split("?")[0].isdigit():
            raise InvalidLink(f"unsupported scheme: {prefix.group(1)}")
        text = "https://" + text
    try:
        parsed = urlparse(text)
        host, port = parsed.hostname, parsed.port
    except ValueError as error:
        raise InvalidLink(f"invalid url: {error}") from error
    if parsed.scheme not in SCHEMES:
        raise InvalidLink(f"unsupported scheme: {parsed.scheme}")
    if not host:
        raise InvalidLink("no host in the url")
    host = host.lower()
    netloc = f"[{host}]" if ":" in host else host
    if port is not None:
        netloc = f"{netloc}:{port}"
    path = parsed.path or "/"
    return urlunparse((parsed.scheme.lower(), netloc, path, parsed.params, parsed.query, ""))


def parse_tags(text: str | None) -> tuple:
    """`a, b a` -> ('a', 'b'). Sorted, lowercase, no duplicates, no blows."""
    if not text:
        return ()
    seen = []
    for piece in text.replace(",", " ").split():
        tag = piece.strip().lower()
        if tag and tag not in seen:
            seen.append(tag)
    return tuple(sorted(seen))


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def looks_readable(link: Link) -> bool:
    """A link is worth keeping when it has a title or a note; a bare url is not."""
    return bool(link.title.strip() or link.note.strip())
