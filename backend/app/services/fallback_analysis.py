"""Safe user-facing analysis returned when the AI provider is unavailable."""

from typing import Any

UNAVAILABLE_MESSAGE = "AI analysis is temporarily unavailable. Your project intake is still ready—please retry shortly."


def unavailable_analysis() -> dict[str, Any]:
    return {
        "Project Overview": "AI analysis is temporarily unavailable.",
        "Structured Analysis": {"Opportunity": "Compass could not reach the AI service right now.", "Core user": "Not assessed while the AI service is unavailable.", "Scope recommendation": "Keep your current idea and retry analysis shortly."},
        "Assumptions": ["No AI-generated assumptions are available until the service reconnects."],
        "Transparent Reasoning": ["Compass is showing a safe fallback because the AI provider did not return an analysis."],
        "Red Flags": ["Live AI analysis is unavailable; do not treat this fallback as project advice."],
        "Recommended MVP Roadmap": [{"Step": "Retry analysis", "Outcome": "Receive a tailored project plan when Gemini is available."}],
        "Project Journey": ["Project intake submitted", "AI analysis temporarily unavailable", "Retry when service recovers"],
        "What's Next": ["Check your Gemini API key, quota, and connection, then select Analyze Project again."],
    }
