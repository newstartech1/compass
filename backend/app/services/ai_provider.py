"""Minimal contract that makes Compass's AI provider replaceable."""

from typing import Any, Protocol


class AIProviderUnavailable(Exception):
    """Raised when an AI provider cannot produce an analysis right now."""


class ProjectAnalysisProvider(Protocol):
    def analyze(self, intake: dict[str, Any]) -> dict[str, Any]:
        """Return Compass analysis JSON or raise AIProviderUnavailable."""
