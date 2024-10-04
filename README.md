# claims-managment

This is a Ticket System application built with Flask for the backend and a modern frontend interface. It uses MongoDB for data storage and Docker for containerization, allowing each part of the application to run in its own environment.

## Project Structure
. ├── backend/ │ 
    ├── app.py │ 
    ├── docker-compose.yml 
    ├── Dockerfile 
    ├── requirements.txt 

  └── frontend/
    ├── Dockerfile 
    ├── css/ 
        │ └── styles.css 
    ├── js/ 
        │ └── app.js
        │ └── api.js
    └── index.html

## Technologies Used

- **Backend**: Flask, MongoDB
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setting Up the Backend

1. Navigate to the `backend` directory:
    cd backend
    docker-compose up --build
2. Navigate to the frontend directory:
    cd frontend
    docker-compose up --build