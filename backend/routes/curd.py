from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.models.models import Task
from backend.schemas.schemas import TaskCreate
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def post_task(task_data :TaskCreate,db :Session):

    tasks = Task(
        task = task_data.task,
        status = task_data.status
        )

    db.add(tasks)
    db.commit()

    logger.info("task has been created")
    return {"messege":"task has been added"},200

def read_tasks(db :Session):

    tasks = db.query(Task).all()

    return tasks

def update_task(task_data :TaskCreate,Task_id : int,db :Session):

    task = db.query(Task).filter(Task.id == Task_id).first()

    if not task:
        loggger.warning("task not found")
        raise HTTPException(
            status_code=404,
            detail="task not found"
            )

    task.task = task_data.task
    task.status = task_data.status

    db.commit()

    if task.status == "Completed":
        logger.info("task has been completed")
    else:
        logger.info("task has been updated")

    return {"messege":"task has been updated"},200

def delete_task(Task_id : int,db :Session):

    task = db.query(Task).filter(Task.id == Task_id).first()

    if not task:
        logger.warning("task not found")
        raise HTTPException(
            status_code=404,
            detail="task not found"
            )

    db.delete(task)
    db.commit()

    logger.info("task has been deleted")
    return {"messege":"task has been deleted"},200




