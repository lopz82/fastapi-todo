from typing import List

import uvicorn as uvicorn
from fastapi import FastAPI, Depends, Path

import models
import schemas
import services
from database import engine
from dependencies import get_repository
from type_hints import Repository

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/taskslists", response_model=schemas.TasksList, status_code=201)
def create_tasks_list(
    tasks_list: schemas.TasksListCreate, repo: Repository = Depends(get_repository)
):
    return services.create_tasks_list(repo, tasks_list)


@app.get("/taskslists", response_model=List[schemas.TasksList])
def get_all_tasks_lists(repo: Repository = Depends(get_repository)):
    return services.get_all_tasks_lists(repo)


@app.get("/taskslists/{tasks_list_id}", response_model=schemas.TasksList)
def get_tasks_list(
    tasks_list_id: int = Path(..., title="Tasks list ID", gt=0),
    repo: Repository = Depends(get_repository),
):
    return services.get_tasks_list(repo, tasks_list_id)


@app.patch("/taskslists/{tasks_list_id}", response_model=schemas.TasksList)
def patch_tasks_list(
    tasks_list: schemas.TasksListCreate,
    tasks_list_id: int = Path(..., title="Tasks list ID", gt=0),
    repo: Repository = Depends(get_repository),
):
    return services.update_tasks_list(repo, tasks_list_id, tasks_list.dict())


@app.put("/taskslists/{tasks_list_id}", response_model=schemas.TasksList)
def put_tasks_list(
    tasks_list: schemas.TasksListCreate,
    tasks_list_id: int = Path(..., title="Tasks list ID", gt=0),
    repo: Repository = Depends(get_repository),
):
    return services.replace_tasks_list(repo, tasks_list_id, tasks_list)


@app.delete("/taskslists/{tasks_list_id}")
def delete_tasks_list(
    tasks_list_id: int = Path(..., title="Tasks list ID", gt=0),
    repo: Repository = Depends(get_repository),
):
    services.delete_tasks_list(repo, tasks_list_id)


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=8080)
