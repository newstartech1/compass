"""FastAPI entry point for Compass."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import allowed_origins
from app.routers.analysis import router as analysis_router
from app.routers.health import router as health_router

app = FastAPI(
    title="Compass API",
    description="AI-powered project navigation assistant.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(analysis_router, prefix="/api")


@app.get("/", tags=["system"])
async def root() -> dict[str, str]:
    return {"message": "Compass API is online. Visit /docs for the API reference."}
