# Task Manager API

A simple REST API built using Flask and SQLite to manage tasks.

## Features
- Create a task (POST /tasks)
- Get all tasks (GET /tasks)
- Update a task (PUT /tasks/<id>)
- Delete a task (DELETE /tasks/<id>)

## Tech Stack
- Python
- Flask
- SQLite

## Functionality
- Performs CRUD operations
- Validates user input
- Uses proper HTTP status codes
- Handles errors (invalid input, task not found)

## Example Request

POST /tasks

json {   "task": "study" } 

## Example Response

json {   "success": true,   "message": "task added" } 

## How to Run

1. Install dependencies:
bash pip install flask 

2. Run the server:
bash python app.py 

3. Open in browser or Postman:
http://127.0.0.1:5000/tasks

## Purpose

This project was built to understand backend development, API design, and database integration using Python.