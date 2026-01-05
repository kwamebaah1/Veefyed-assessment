from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import logging
import os
from typing import List, Optional

from app.services.analysis_service import perform_mock_analysis
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

class AnalyzeRequest(BaseModel):
    image_id: str

@router.post("/analyze")
async def analyze_image(request: AnalyzeRequest):
    """
    Analyze an uploaded image by image_id
    Returns: Analysis results including skin type, issues, and confidence
    """
    try:
        image_id = request.image_id
        logger.info(f"Received analysis request for image_id: {image_id}")
        
        # Check if image exists
        image_path = None
        for ext in ['.jpg', '.jpeg', '.png']:
            possible_path = os.path.join("app/storage/images", f"{image_id}{ext}")
            if os.path.exists(possible_path):
                image_path = possible_path
                break
        
        if not image_path:
            logger.warning(f"Image not found for image_id: {image_id}")
            raise HTTPException(
                status_code=404,
                detail=f"Image with ID {image_id} not found"
            )
        
        logger.info(f"Found image at: {image_path}")
        
        # Perform mock analysis
        analysis_result = perform_mock_analysis(image_id, image_path)
        
        logger.info(f"Analysis completed for image_id: {image_id}")
        
        return {
            "image_id": image_id,
            "analysis": analysis_result,
            "message": "Analysis completed successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error during analysis"
        )