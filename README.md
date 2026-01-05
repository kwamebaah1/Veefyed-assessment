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