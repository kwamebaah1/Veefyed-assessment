import os
import random
import logging
from typing import List, Dict, Any
from datetime import datetime

from app.utils.logger import get_logger

logger = get_logger(__name__)

# Mock data for analysis
SKIN_TYPES = ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
SKIN_ISSUES = [
    "Hyperpigmentation", 
    "Acne", 
    "Fine Lines", 
    "Dark Spots", 
    "Redness", 
    "Pores", 
    "Uneven Texture"
]

def perform_mock_analysis(image_id: str, image_path: str) -> Dict[str, Any]:
    """
    Perform mock analysis on an image.
    In a real implementation, this would call an AI/ML model.
    """
    try:
        logger.info(f"Starting mock analysis for: {image_path}")
        
        file_size = os.path.getsize(image_path)
        file_extension = os.path.splitext(image_path)[1]
        
        # Generate deterministic but varied results based on image_id
        # Using hash of image_id to make results consistent for same ID
        seed_value = hash(image_id) % 10000
        random.seed(seed_value)
        
        # Mock analysis logic
        skin_type = random.choice(SKIN_TYPES)
        
        # Select 1-3 random issues
        num_issues = random.randint(1, 3)
        issues = random.sample(SKIN_ISSUES, num_issues)
        
        # Generate confidence score
        confidence = round(random.uniform(0.75, 0.95), 2)
        
        # Generate mock metrics
        analysis_details = {
            "skin_type": skin_type,
            "skin_type_confidence": round(random.uniform(0.8, 0.98), 2),
            "detected_issues": issues,
            "overall_confidence": confidence,
            "analysis_timestamp": datetime.utcnow().isoformat() + "Z",
            "file_info": {
                "size_bytes": file_size,
                "format": file_extension[1:].upper(),
                "analyzed": True
            },
            "mock_metrics": {
                "hydration_level": round(random.uniform(0.4, 0.9), 2),
                "oiliness_level": round(random.uniform(0.3, 0.8), 2),
                "evenness_score": round(random.uniform(0.5, 0.95), 2)
            }
        }
        
        logger.info(f"Analysis generated for {image_id}: {skin_type} skin, {len(issues)} issues")
        
        return analysis_details
        
    except Exception as e:
        logger.error(f"Error in mock analysis: {str(e)}")
        return {
            "skin_type": "Unknown",
            "skin_type_confidence": 0.0,
            "detected_issues": ["Analysis Failed"],
            "overall_confidence": 0.0,
            "analysis_timestamp": datetime.utcnow().isoformat() + "Z",
            "error": "Analysis could not be completed"
        }