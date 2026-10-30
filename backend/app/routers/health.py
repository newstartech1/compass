"""Health and readiness routes."""

from datetime import UTC, datetime

from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Confirm that the Compass API is available."""
    return {
        "status": "ok",
        "service": "compass-api",
        "timestamp": datetime.now(UTC).isoformat(),
    }

