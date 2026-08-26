Perfect. 🔥 Here is the **final shorter README** with your live Render URL and the correct current structure:

````markdown
# 🚀 Task Manager API

A full-stack task management application built with **FastAPI, PostgreSQL, SQLAlchemy, Pydantic, HTML, CSS, and JavaScript**.

The project was originally built with Flask + SQLite and later upgraded to FastAPI + PostgreSQL.

## 🌐 Live API

https://task-manager-api-1-xy2g.onrender.com

## ✨ Features

- Create tasks
- View tasks
- Edit tasks
- Complete tasks
- Delete tasks
- PostgreSQL database
- SQLAlchemy ORM
- Pydantic validation
- CORS
- Responsive frontend
- Environment variables

## 🛠️ Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy, Pydantic, PostgreSQL

**Frontend:** HTML, CSS, JavaScript

**Deployment:** GitHub, Render

## 🏗️ Architecture

```text
Frontend
   ↓
FastAPI
   ↓
CRUD
   ↓
SQLAlchemy
   ↓
PostgreSQL
````

## 📁 Project Structure

```text
task-manager-api/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── curd.py
│   └── init_db.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
└── .env
```

> `.env` is kept locally and is not uploaded to GitHub.

## 🔌 API Endpoints

| Method | Endpoint      | Description   |
| ------ | ------------- | ------------- |
| GET    | `/`           | Get all tasks |
| POST   | `/tasks`      | Create a task |
| PUT    | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

### Create Task

```json
{
    "task": "Learn PostgreSQL"
}
```

If no status is provided, it defaults to `pending`.

### Update / Complete Task

```json
{
    "task": "Learn FastAPI",
    "status": "Completed"
}
```

## 🗄️ Database

The application uses **PostgreSQL** with **SQLAlchemy ORM**.

The database URL is provided through the environment variable:

```env
DATABASE_URL=your_database_url
```

## 💻 Run Locally

```bash
git clone <your-repository-url>
cd task-manager-api

pip install -r requirements.txt

uvicorn backend.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
https://task-manager-api-1-xy2g.onrender.com/docs
```

## 📸 Screenshots

### Task Manager

![Task Manager](screenshots/frontend.png)

### API Documentation

![FastAPI Swagger](screenshots/swagger.png)

## 🔄 Project Upgrade

**Before:**

`Flask + SQLite`

**Now:**

`FastAPI + PostgreSQL + SQLAlchemy + Pydantic`

## 👨‍💻 Author

**Sabir Ahmed**

BCA Student | Backend Developer





