from fastapi import APIRouter, File, UploadFile, HTTPException
import logging
import uuid
import os

from app.utils.file_utils import validate_image_file
from app.utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

# Create storage directory if it doesn't exist
os.makedirs("app/storage/images", exist_ok=True)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image file (JPEG or PNG, max 5MB)
    Returns: {"image_id": "unique_id"}
    """
    try:
        logger.info(f"Received upload request for file: {file.filename}")
        
        # Validate file type and MIME
        validation_result = await validate_image_file(file)
        if not validation_result["valid"]:
            logger.warning(f"File validation failed: {validation_result['message']}")
            raise HTTPException(
                status_code=400,
                detail=validation_result["message"]
            )
        
        # Read file content to check size
        contents = await file.read()
        file_size = len(contents)
        
        # Check file size (5MB limit)
        MAX_FILE_SIZE = 5 * 1024 * 1024
        if file_size > MAX_FILE_SIZE:
            logger.warning(f"File size exceeds limit: {file_size} bytes")
            raise HTTPException(
                status_code=400,
                detail=f"File size exceeds {MAX_FILE_SIZE // (1024*1024)}MB limit"
            )
        
        # Reset file pointer after reading
        await file.seek(0)
        
        # Generate unique ID for the image
        image_id = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[1].lower()
        filename = f"{image_id}{file_extension}"
        file_path = os.path.join("app/storage/images", filename)
        
        # Save the file
        with open(file_path, "wb") as f:
            f.write(contents)
        
        logger.info(f"Image saved successfully: {filename}")
        
        return {
            "image_id": image_id,
            "filename": filename,
            "message": "Image uploaded successfully"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error during upload: {str(e)}"
        )
