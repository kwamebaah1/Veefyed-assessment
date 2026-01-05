# Image Analysis API

A FastAPI-based backend service for uploading images and performing mock skin analysis. This project demonstrates backend API design, file handling, and integration patterns.

## Features

- **Image Upload**: Accepts JPEG/PNG images up to 5MB
- **Mock Analysis**: Returns structured skin analysis data
- **Error Handling**: Comprehensive validation and error responses
- **Logging**: Basic request/error logging
- **Docker Support**: Containerized deployment

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)

## Installation & Setup

### Local Development

1. **Clone and setup environment:**
```bash
git clone <repository-url>
cd image-analysis-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

2. **Run the application:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
## Using Docker

1. **Build the Docker image:**
```bash
docker build -t image-analysis-api .
```
2. **Run the container:**
```bash
docker run -p 8000:8000 image-analysis-api
```

## API Endpoints
1. Upload Image
POST /api/v1/upload

Uploads an image file for analysis.

Request:

Content-Type: multipart/form-data

Body: file (image file, max 5MB, JPEG/PNG)

Response (Success):
```bash
{
  "image_id": "123e4567-e89b-12d3-a456-426614174000",
  "filename": "123e4567-e89b-12d3-a456-426614174000.jpg",
  "message": "Image uploaded successfully"
}
```