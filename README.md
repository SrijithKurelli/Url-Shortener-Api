# URL Shortener API

A RESTful URL shortening service built with FastAPI and PostgreSQL that generates short URLs, redirects users, and provides URL analytics.

## Project Overview

This project is a backend REST API that allows users to generate shortened links from long URLs. Each generated short URL redirects users to the original destination while tracking analytics such as click count and last accessed time. The application follows a layered architecture with separate API, service, model, schema, and database layers, making the codebase modular and easy to maintain.

## Features

- Generate unique 6-character short URLs
- Redirect users to the original URL
- Track click count for each shortened URL
- Track the last accessed timestamp
- Retrieve URL analytics through a dedicated API endpoint
- PostgreSQL database integration using SQLAlchemy ORM
- Request validation using Pydantic
- Interactive API documentation with Swagger UI

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL

### Libraries
- Pydantic
- psycopg2
- python-dotenv

### Tools
- Swagger UI
- Postman

## Project Structure

```text
URL-Shortener/
│
├── app/
│   ├── api/          # API route definitions
│   ├── core/         # Configuration
│   ├── db/           # Database connection
│   ├── models/       # SQLAlchemy models
│   ├── schemas/      # Pydantic schemas
│   ├── services/     # Business logic
│   ├── utils/        # Utility functions
│   └── main.py       # FastAPI entry point
│
├── docs/             # Postman collection
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/health` | Checks database connectivity |
| POST | `/shorten` | Creates a shortened URL |
| GET | `/{short_code}` | Redirects to the original URL |
| GET | `/analytics/{short_code}` | Returns analytics for a shortened URL |

## Design Decisions

- Duplicate URLs generate unique short codes instead of reusing existing ones.
- The project follows a layered architecture by separating routes, business logic, models, schemas, and database configuration.
- PostgreSQL is used as the persistent data store with SQLAlchemy as the ORM.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SrijithKurelli/Url-Shortener-Api
cd URL-Shortener
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Copy `.env.example` and rename it to `.env`, then update the values according to your PostgreSQL configuration.

## Running the Project

Start the development server:

```bash
uvicorn app.main:app --reload
```

Once the server starts, the API will be available at:

- Base URL: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`

## Postman Collection

A Postman collection containing all API endpoints is available in the `docs/` directory for testing the application.

## Future Improvements

- Support custom short URLs
- Implement URL expiration
- Add rate limiting
- Containerize the application using Docker
- Add user authentication and URL management
