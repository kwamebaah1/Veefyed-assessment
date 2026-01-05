from fastapi import UploadFile
import os
from typing import Dict

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

async def validate_image_file(file: UploadFile) -> Dict:
    """
    Validate uploaded image file
    Returns: {"valid": bool, "message": str}
    """
    try:
        # Check file extension
        file_extension = os.path.splitext(file.filename)[1].lower()
        if file_extension not in ALLOWED_EXTENSIONS:
            return {
                "valid": False,
                "message": f"Invalid file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
            }
        
        # Check MIME type
        content_type = file.content_type
        allowed_mime_types = ["image/jpeg", "image/jpg", "image/png"]
        if content_type not in allowed_mime_types:
            return {
                "valid": False,
                "message": f"Invalid MIME type. Allowed: {', '.join(allowed_mime_types)}"
            }
        
        return {"valid": True, "message": "File validation successful"}
        
    except Exception as e:
        return {
            "valid": False,
            "message": f"Error validating file: {str(e)}"
        }
