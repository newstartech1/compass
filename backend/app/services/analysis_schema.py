"""Provider-neutral response contract for a Compass analysis."""

from typing import Any

ANALYSIS_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "Project Overview": {"type": "string"},
        "Structured Analysis": {"type": "object", "properties": {"Opportunity": {"type": "string"}, "Core user": {"type": "string"}, "Scope recommendation": {"type": "string"}}, "required": ["Opportunity", "Core user", "Scope recommendation"]},
        "Assumptions": {"type": "array", "items": {"type": "string"}},
        "Transparent Reasoning": {"type": "array", "items": {"type": "string"}},
        "Red Flags": {"type": "array", "items": {"type": "string"}},
        "Recommended MVP Roadmap": {"type": "array", "items": {"type": "object", "properties": {"Step": {"type": "string"}, "Outcome": {"type": "string"}}, "required": ["Step", "Outcome"]}},
        "Project Journey": {"type": "array", "items": {"type": "string"}},
        "What's Next": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["Project Overview", "Structured Analysis", "Assumptions", "Transparent Reasoning", "Red Flags", "Recommended MVP Roadmap", "Project Journey", "What's Next"],
}

SYSTEM_PROMPT = """You are Compass, an AI-powered project navigator for builders and innovation teams. Analyze the submitted intake to help the team make better project decisions. Prioritize a realistic, compelling demo within the stated time, skills, technologies, and constraints. Be specific and practical. Do not invent facts or integrations; identify uncertainty as an assumption. Cover structured reasoning, transparent analysis, assumptions, risks, MVP planning, the project journey, and likely future challenges. For 'Transparent Reasoning', provide 2-4 concise, user-facing decision rationales grounded in the intake. Do not reveal private chain-of-thought or hidden reasoning. Return only JSON that matches the provided schema."""
