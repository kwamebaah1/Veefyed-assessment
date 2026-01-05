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

### Testing the API
## Using Swagger UI (Interactive Testing)

FastAPI automatically generates interactive API documentation at /docs. This is the easiest way to test the endpoints:

Start the server using either local development or Docker method above.

Open your browser and navigate to: http://localhost:8000/docs

You'll see the Swagger UI with all available endpoints.

**Testing Upload Endpoint:**
```bash
Click on the "POST /api/v1/upload" endpoint

Click the "Try it out" button

Click "Choose File" and select an image (JPG or PNG, under 5MB)

Click "Execute"

Copy the image_id from the response
```

**Testing Analyze Endpoint:**
```bash
Click on the "POST /api/v1/analyze" endpoint

Click the "Try it out" button

Paste the image_id from the upload response into the request body

Click "Execute"

View the mock analysis results
```

## API Endpoints

### 1. Upload Image
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

### 2. Analyze Image
POST /api/v1/analyze

Performs mock analysis on an uploaded image.

Request:
```bash
{
  "image_id": "123e4567-e89b-12d3-a456-426614174000"
}
```
Response (Success):
```bash
{
  "image_id": "123e4567-e89b-12d3-a456-426614174000",
  "analysis": {
    "skin_type": "Oily",
    "skin_type_confidence": 0.92,
    "detected_issues": ["Hyperpigmentation", "Acne"],
    "overall_confidence": 0.87,
    "analysis_timestamp": "2024-01-01T12:00:00Z",
    "file_info": {
      "size_bytes": 123456,
      "format": "JPEG",
      "analyzed": true
    },
    "mock_metrics": {
      "hydration_level": 0.76,
      "oiliness_level": 0.82,
      "evenness_score": 0.68
    }
  },
  "message": "Analysis completed successfully"
}
```

### Error Responses
400 Bad Request: Invalid file type/size, missing parameters

404 Not Found: Image ID not found

500 Internal Server Error: Server-side processing error