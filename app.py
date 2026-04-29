from flask import Flask,request
import sqlite3 as sq
import os

conn = sq.connect("tasks.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS tasks (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    task TEXT,

    status TEXT

)

""")

conn.commit()

conn.close()


app = Flask(__name__)

@app.route("/")
def get_tasks():
    conn = sq.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    tasks_list = [
        {"id": r[0], "task": r[1], "status": r[2]}
        for r in rows
    ]

    conn.close()

    return {
        "success": True,
        "data": tasks_list
    }, 200

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json

    task = data.get("task") if data else None

    if not task:
        return {
            "success": False,
            "error": "task is required"
        }, 400
    
    conn = sq.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (task, status) VALUES (?, ?)",
        (task, "pending")
    )

    conn.commit()
    conn.close()

    return {
        "success": True,
        "message": "task added"
    }, 201
    
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.json

    if not data:
        return {"success": False, "error": "invalid data"}, 400

    task = data.get("task")
    status = data.get("status")

    if not task or not status:
        return {"success": False, "error": "task and status required"}, 400

    conn = sq.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET task = ?, status = ? WHERE id = ?",
        (task, status, id)
    )

    if cursor.rowcount == 0:
        conn.close()
        return {"success": False, "error": "task not found"}, 404

    conn.commit()
    conn.close()

    return {"success": True, "message": "task updated"}, 200

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    conn = sq.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (id,)
    )

    if cursor.rowcount == 0:
        conn.close()
        return {"success": False, "error": "task not found"}, 404
    
    conn.commit()
    conn.close()

    return {"success": True, "message": "task deleted"}, 200
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
