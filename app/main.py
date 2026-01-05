from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.routes import upload, analyze
from app.utils.logger import setup_logger

# Setup logging
logger = setup_logger()

app = FastAPI(
    title="Image Analysis API",
    description="Backend service for image upload and mock analysis",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router, prefix="/api/v1", tags=["upload"])
app.include_router(analyze.router, prefix="/api/v1", tags=["analyze"])

@app.get("/")
async def root():
    return {
        "message": "Image Analysis API",
        "endpoints": {
            "upload": "POST /api/v1/upload",
            "analyze": "POST /api/v1/analyze"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Image Analysis API")
    uvicorn.run(app, host="0.0.0.0", port=8000)