from fastapi import FastAPI ,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from backend.init_db import init_db
from backend.database import get_db
from backend.schemas import TaskCreate
import backend.curd as curd 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()


@app.post("/tasks")
def post_task(task_data :TaskCreate,
              db :Session = Depends(get_db)
              ):
    return curd.post_task(task_data,db)

                          

@app.get("/")
def read_tasks(db :Session = Depends(get_db)
              ):
    return curd.read_tasks(db)



@app.put("/tasks/{Task_id}")
def update_task(task_data :TaskCreate,
                Task_id :int,
                db :Session = Depends(get_db)
                ):
    return curd.update_task(task_data,Task_id,db)


@app.delete("/tasks/{Task_id}")
def delete_task(Task_id :int,
                db :Session = Depends(get_db)
                ):
    return curd.delete_task(Task_id,db)













                
