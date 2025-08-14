# Outside Code Challenge - NASA APOD API

A Django REST API application that fetches NASA's Astronomy Picture of the Day (APOD) and enhances it with additional Wikipedia data for astronomical objects.

## Overview

This application provides a REST API endpoint that:
- Fetches NASA's Astronomy Picture of the Day for a specified date
- Parses the explanation text to identify astronomical objects (NGC, IC, LEDA catalogs)
- Retrieves additional information from Wikipedia for identified objects
- Stores and returns the enhanced data through a RESTful interface

## Features

- **NASA APOD Integration**: Connects to NASA's APOD API to fetch daily astronomy pictures
- **Wikipedia Enhancement**: Automatically searches Wikipedia for additional information on astronomical objects
- **Date Flexibility**: Supports queries for any date or defaults to today's picture
- **Object Recognition**: Parses text to identify astronomical objects using standard catalog notations
- **Admin Interface**: Django admin panel for data management
- **RESTful API**: Clean API endpoints with proper error handling
- **Comprehensive Testing**: Unit tests with mocking for external API calls

## Tech Stack

- **Framework**: Django 5.2.5
- **API**: Django REST Framework 3.16.1
- **Database**: SQLite (development)
- **External APIs**: NASA APOD API, Wikipedia API
- **Dependencies**: requests, python-dateutil

## Prerequisites

- Python 3.8+ (tested with Python 3.12.2)
- pip (Python package installer)
- Internet connection (for external API calls)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd outsideProject
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Run tests**
   ```bash
   python manage.py test
   ```

## API Usage

### Get Astronomy Picture of the Day

**Endpoint**: `GET /api/picture/`

**Parameters**:
- `date` (optional): Date in YYYY-MM-DD format. Defaults to today if not provided.

**Examples**:
```bash
# Get today's picture
GET /api/picture/

# Get picture for specific date
GET /api/picture/?date=2024-01-01
```

**Response**:
```json
{
    "date": "2024-01-01",
    "title": "Picture Title",
    "explanation": "Detailed explanation of the astronomical image...",
    "url": "https://apod.nasa.gov/apod/image/2401/example.jpg",
    "hdurl": "https://apod.nasa.gov/apod/image/2401/example_hd.jpg",
    "media_type": "image",
    "service_version": "v1",
    "copyright": "Copyright Information",
    "additional_data": "Enhanced Wikipedia data for astronomical objects"
}
```

## Configuration Notes

- **NASA API Key**: Currently using `DEMO_KEY` for development. For production, obtain a free API key from https://api.nasa.gov/ and update `nasa_api.py`
- **Database**: Uses SQLite for development. Consider PostgreSQL or MySQL for production
- **Security**: Debug mode is enabled for development. Disable for production deployment

## Testing

The application includes comprehensive unit tests that mock external API calls to ensure reliable testing without dependencies on external services.
