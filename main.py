import uvicorn as uvicorn
from fastapi import FastAPI, Depends, Path
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine
from dependencies import get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/taskslists", response_model=schemas.TasksList, status_code=201)
def create_tasks_list(
    tasks_lists: schemas.TasksListCreate, db: Session = Depends(get_db)
):
    new_tasklist = crud.create_taskslist(db, tasks_lists)
    return new_tasklist


@app.get("/taskslists/{taskslist_id}", response_model=schemas.TasksList)
def get_tasks_list(
    taskslist_id: int = Path(..., title="Tasks list ID", gt=0),
    db: Session = Depends(get_db),
):
    return crud.get_taskslist(db, taskslist_id)


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=8080)
