"""Compatibility helpers for optional third-party dependencies."""

from __future__ import annotations

try:
    from s3path import S3Path  # type: ignore
except Exception:  # pragma: no cover
    class S3Path:  # type: ignore[no-redef]
        """Fallback placeholder when s3path is unavailable or incompatible."""

        pass
