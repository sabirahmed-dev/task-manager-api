Task Manager CRUD API

A simple REST API built with Flask and SQLite that allows users to create, read, update, and delete tasks.

Features

* Create a new task
* View all tasks
* Update an existing task
* Delete a task
* SQLite database integration
* RESTful API design
* Deployable with Gunicorn and Render

Tech Stack

* Python
* Flask
* SQLite
* Gunicorn
* Render

API Endpoints

Get All Tasks

GET /tasks

Create Task

POST /tasks

Request Body:

{
    "task": "Learn Flask"
}

Update Task

PUT /tasks/<id>

Request Body:

{
    "task": "Learn Flask API",
    "status": "completed"
}

Delete Task

DELETE /tasks/<id>

Installation

Clone the repository:

git clone <your-repository-url>
cd task-manager-api

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Deployment

This project can be deployed on Render using Gunicorn.

Start Command:

gunicorn app:app

Author

Sabir Ahmed
BCA Student | Backend Developer Learning Journey