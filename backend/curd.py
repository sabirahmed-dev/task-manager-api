from sqlalchemy.orm import Session
from backend.models import Task
from backend.schemas import TaskCreate


def post_task(task_data :TaskCreate,db :Session):

    tasks = Task(
        task = task_data.task,
        status = task_data.status
        )

    db.add(tasks)
    db.commit()

    return {"messege":"task has been added"},200

def read_tasks(db :Session):

    tasks = db.query(Task).all()

    return tasks

def update_task(task_data :TaskCreate,Task_id : int,db :Session):

    task = db.query(Task).filter(Task.id == Task_id).first()

    if not task:
        return {"message": "User not found"}

    task.task = task_data.task
    task.status = task_data.status

    db.commit()

    return {"messege":"task has been updated"},200

def delete_task(Task_id : int,db :Session):

    task = db.query(Task).filter(Task.id == Task_id).first()

    if not task:
        return {"message": "User not found"}

    db.delete(task)
    db.commit()
    
    return {"messege":"task has been deleted"},200
    
     
        
    
