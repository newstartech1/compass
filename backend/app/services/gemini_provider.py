"""Gemini implementation of the provider-neutral Compass AI contract."""

import json
import logging
import os
from typing import Any

from google import genai
from google.genai import types

from app.services.ai_provider import AIProviderUnavailable
from app.services.analysis_schema import ANALYSIS_SCHEMA, SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class GeminiProjectAnalysisProvider:
    """Generate structured Compass analyses through the Gemini API."""

    def __init__(self) -> None:
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    def analyze(self, intake: dict[str, Any]) -> dict[str, Any]:
        if not self.api_key:
            raise AIProviderUnavailable("Gemini is not configured.")
        try:
            client = genai.Client(api_key=self.api_key)
            response = client.models.generate_content(
                model=self.model,
                contents=f"{SYSTEM_PROMPT}\n\nPROJECT INTAKE:\n{json.dumps(intake, ensure_ascii=False)}",
                config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=ANALYSIS_SCHEMA),
            )
            analysis = response.parsed or json.loads(response.text)
            if not isinstance(analysis, dict):
                raise ValueError("Gemini did not return an analysis object.")
            return analysis
        except Exception as error:
            logger.warning("Gemini analysis is unavailable: %s", error)
            raise AIProviderUnavailable("Gemini analysis is temporarily unavailable.") from error
