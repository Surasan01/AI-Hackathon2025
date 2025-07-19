# AI-Hackathon2025
```
AI-Hackathon2025/
├── README.md
└── hackathon-quiz/
    ├── docker-compose.yml
    ├── api1/
    │   ├── Dockerfile
    │   ├── main.py
    │   └── requirements.txt
    └── api2/
        ├── Dockerfile
        ├── main.py
        └── requirements.txt
```

## Services

### API1 (Port 8000)
- **Description**: Gateway service that forwards requests to API2
- **Endpoint**: `GET /`
- **Function**: Receives requests and forwards them to API2 service
- **Dependencies**: Requires API2 to be running

### API2 (Port 8001)
- **Description**: Backend service that handles the actual business logic
- **Endpoint**: `GET /`
- **Function**: Returns a simple greeting message

## Prerequisites

- Docker
- Docker Compose

## Installation & Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd AI-Hackathon2025/hackathon-quiz
```

2. Build and run the services:
```bash
docker-compose up --build
```

3. The services will be available at:
   - API1: http://localhost:8000
   - API2: http://localhost:8001

## Usage

### Test API1 (Gateway)
```bash
curl http://localhost:8000/
```
This will forward the request to API2 and return: `{"message": "Hello from API 2"}`

### Test API2 (Direct)
```bash
curl http://localhost:8001/
```
This will directly return: `{"message": "Hello from API 2"}`

## Development

### Running Services Individually

#### API1
```bash
cd api1
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### API2
```bash
cd api2
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001
```

### Dependencies

#### API1
- fastapi
- uvicorn
- httpx

#### API2
- fastapi
- uvicorn

## Architecture

The project follows a simple microservices pattern:

1. **API1** acts as a gateway/proxy service
2. **API2** provides the core functionality
3. Communication between services happens over HTTP
4. Services are containerized using Docker
5. Docker Compose orchestrates the multi-container setup

## Docker Configuration

- Both services use Python 3.9-slim base image
- Services communicate using Docker's internal network
- API1 depends on API2 (startup order managed by Docker Compose)