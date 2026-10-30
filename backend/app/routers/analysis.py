"""Project analysis API powered by NVIDIA Nemotron through Nebius."""

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.ai_provider import AIProviderUnavailable
from app.services.fallback_analysis import (
    UNAVAILABLE_MESSAGE,
    unavailable_analysis,
)
from app.services.nebius_provider import NebiusProjectAnalysisProvider

router = APIRouter(tags=["analysis"])


class ProjectIntake(BaseModel):
    idea: str = Field(min_length=10, max_length=4000)
    category: str = Field(min_length=1, max_length=100)
    available_time: str = Field(
        alias="availableTime", min_length=1, max_length=100
    )
    team_size: str = Field(alias="teamSize", default="Just me", max_length=100)
    skills: str = Field(default="", max_length=1000)
    technologies: str = Field(default="", max_length=1000)
    constraints: str = Field(default="", max_length=2000)
    goals: str = Field(default="", max_length=2000)


@router.post("/analyze")
async def analyze_project(intake: ProjectIntake) -> dict[str, Any]:
    try:
        analysis = NebiusProjectAnalysisProvider().analyze(
            intake.model_dump()
        )
        return {
            "analysis": analysis,
            "ai_available": True,
            "provider": "Nebius Token Factory",
            "model": "NVIDIA Nemotron",
            "message": "Your Compass analysis is ready.",
        }
    except AIProviderUnavailable:
        return {
            "analysis": unavailable_analysis(),
            "ai_available": False,
            "provider": "Nebius Token Factory",
            "message": UNAVAILABLE_MESSAGE,
        }
