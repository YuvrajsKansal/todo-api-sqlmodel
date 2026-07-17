from contextlib import asynccontextmanager
from datetime import date, datetime
from typing import Annotated, Optional
from fastapi import Depends, FastAPI,HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, Session, create_engine,Field, select

engine = create_engine("sqlite:///tasks.db")

class Task_db(SQLModel,table =True):
    id :Optional[int] = Field(default = None,primary_key = True)
    title :str = Field(default=None)
    due_date:date = Field(default=None)
    description:str = Field(default=None)

@asynccontextmanager
async def lifespan(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
app=FastAPI(lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]
class Task(BaseModel):
    title :str = Field(default=None)
    due_date: date = Field(default=None)
    description:str = Field(default=None)


@app.get("/tasks")
def get_tasks(session:SessionDep):
    data=session.exec(select(Task_db)).all()
    return{"tasks":data}

@app.get("/tasks/{task_id}")
def get_one_task(task_id:int,session:SessionDep):
    data = session.get(Task_db,task_id)
    if not data:
        raise HTTPException(status_code=404,detail="task not found")
    return {"task":data}
    

        
@app.post("/tasks")
def add_task(task:Task, session:SessionDep):
    new_task = Task_db(**task.model_dump())
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return {"message":f"added {new_task} to tasks"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int,session:SessionDep):
    data = session.get(Task_db,task_id)
    if not data:
        raise HTTPException(status_code=404,detail="task not found")
    session.delete(data)
    session.commit()
    return {"message":f"Task {task_id} deleted"}
    
@app.put("/tasks/{task_id}")
def update_task(task_id:int,task:Task,session:SessionDep):
    data = session.get(Task_db,task_id)
    if not data:
            raise HTTPException(status_code=404,detail="task not found")
    data.title = task.title
    data.due_date = task.due_date
    data.description = task.description
    session.add(data)
    session.commit()
    session.refresh(data)
    return {"message":f"updated task {task_id}"}
    
