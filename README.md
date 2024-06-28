# Task Management Backend (Flask)

## Introduction

Welcome to the backend server for the Task Management application. This Flask-based backend provides a robust API for managing tasks, integrating seamlessly with a PostgreSQL database for data storage and retrieval. The application is designed to handle CRUD (Create, Read, Update, Delete) operations for tasks, offering secure endpoints and scalable deployment on Render.

## Technologies Used

- **Flask**: Python web framework chosen for its simplicity and flexibility in building RESTful APIs.
- **PostgreSQL**: A powerful open-source relational database used to store and manage task data.
- **SQLAlchemy**: An ORM (Object-Relational Mapping) library used with Flask to interact with the PostgreSQL database.
- **Render**: A modern platform used for deploying and hosting applications with built-in scaling and collaboration features.

## Features

### CRUD Operations

- **Create**: Endpoint to add new tasks to the database.
- **Read**: APIs to fetch individual tasks or all tasks from the database.
- **Update**: Endpoint to modify existing tasks based on task ID.
- **Delete**: API to remove tasks from the database by task ID.

### Database Integration

- **Models**: SQLAlchemy models defined for tasks, ensuring structured data storage.
- **Relationships**: Handling relationships and constraints within the PostgreSQL database.

### Security

- **Authentication**: Secured endpoints with appropriate authentication mechanisms.

### Scalability and Deployment

- **Render Deployment**: Deployed on Render for scalability, automatic SSL, and global CDN support.
- **Configuration Management**: Environment variables managed securely within Render for sensitive data.

## Project Structure

The project follows a structured layout:

- **`app/`**: Contains the core application logic.
  - **`models.py`**: Defines SQLAlchemy models for tasks and database relationships.
  - **`routes.py`**: Implements API routes and request handling logic.
- **`config.py`**: Configuration file for database connections, environment variables, and Flask settings.
- **`requirements.txt`**: Lists all Python dependencies required to run the application.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python (version 3.7 or higher)
- pip (Python package installer)
- PostgreSQL database (with a user and database created)

## Getting Started

To set up the project locally:

1. **Clone the Repository**: `git clone <repository_url>`
2. **Install Dependencies**: Navigate to the project directory and run `pip install -r requirements.txt`.
3. **Database Configuration**: Update `config.py` with your PostgreSQL database credentials.
4. **Run the Application**: Execute `flask run` to start the Flask server locally.

## API Documentation

### Endpoints

- `GET /api/tasks`: Retrieves all tasks stored in the database.
- `GET /api/tasks/<task_id>`: Retrieves a specific task by its unique ID.
- `POST /api/tasks/add`: Creates a new task entry in the database.
- `PUT /api/tasks/<task_id>`: Updates an existing task based on its ID.
- `DELETE /api/tasks/<task_id>`: Deletes a task from the database using its ID.

Each endpoint is designed to handle specific HTTP methods (GET, POST, PUT, DELETE) for CRUD operations on tasks.

## Deployment

### Deploying on Render

1. **Create Render Account**: Sign up on Render and create a new web service.
2. **Environment Configuration**: Set up environment variables for database connection details.
3. **GitHub Integration**: Connect your GitHub repository to Render for automatic deployments.
4. **Deployment**: Trigger deployments directly from your `main` branch on each code push.

