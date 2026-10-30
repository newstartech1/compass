"""NVIDIA Nemotron analysis through Nebius Token Factory."""

import json
import os
from typing import Any

from openai import OpenAI

from app.services.ai_provider import AIProviderUnavailable
from app.services.analysis_schema import ANALYSIS_SCHEMA, SYSTEM_PROMPT


class NebiusProjectAnalysisProvider:
    def __init__(self) -> None:
        self.api_key = os.getenv("NEBIUS_API_KEY")
        self.model = os.getenv(
            "NEBIUS_MODEL",
            "nvidia/nemotron-3-super-120b-a12b",
        )

    def analyze(self, intake: dict[str, Any]) -> dict[str, Any]:
        if not self.api_key:
            raise AIProviderUnavailable("Nebius API key is missing.")

        try:
            client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.tokenfactory.us-central1.nebius.com/v1/",
                timeout=90.0,
            )

            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            SYSTEM_PROMPT
                            + "\nReturn a JSON object matching this schema: "
                            + json.dumps(ANALYSIS_SCHEMA)
                        ),
                    },
                    {
                        "role": "user",
                        "content": json.dumps(intake, ensure_ascii=False),
                    },
                ],
                temperature=0.2,
                max_tokens=3000,
            )

            content = response.choices[0].message.content
            if not content:
                raise ValueError("Nebius returned an empty response.")

            content = content.strip()
            if content.startswith("```"):
                content = content.split("\n", 1)[1]
                content = content.rsplit("```", 1)[0].strip()

            analysis = json.loads(content)

            if not isinstance(analysis, dict):
                raise ValueError("Invalid analysis response.")

            missing = set(ANALYSIS_SCHEMA["required"]) - set(analysis)
            if missing:
                raise ValueError(f"Missing sections: {missing}")

            return analysis

        except Exception as error:
            raise AIProviderUnavailable(
                f"Nebius analysis failed: {type(error).__name__}"
            ) from error
