"""Small, dependency-free application configuration."""

import os


def allowed_origins() -> list[str]:
    """Return browser origins permitted to call the API."""
    configured = os.getenv(
        "ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
    )
    return [origin.strip() for origin in configured.split(",") if origin.strip()]

