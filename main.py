from typing import List

import uvicorn as uvicorn
from fastapi import FastAPI, Depends, Path, HTTPException

import models
import schemas
import services
from database import engine
from dependencies import get_repository, get_users_repository
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
    res = services.get_tasks_list(repo, tasks_list_id)
    if not res:
        raise HTTPException(status_code=404, detail="Item not found")
    return res


@app.patch("/taskslists/{tasks_list_id}", response_model=schemas.TasksList)
def patch_tasks_list(
    tasks_list: schemas.TasksListPatch,
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


@app.post("/users", response_model=schemas.User, status_code=201)
def create_user(
    user: schemas.UserCreate, repo: Repository = Depends(get_users_repository)
):
    return services.create_user(repo, user)


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(
    user_id: int = Path(..., title="User ID", gt=0),
    repo: Repository = Depends(get_users_repository),
):
    try:
        res = services.get_user(repo, user_id)
    except services.UserNotFound:
        raise HTTPException(status_code=404, detail="Item not found")
    return res


@app.get("/users", response_model=List[schemas.User])
def get_all_users(repo: Repository = Depends(get_users_repository)):
    return services.get_all_users(repo)


@app.patch("/users/{user_id}", response_model=schemas.User)
def patch_user(
    user: schemas.UserPatch,
    user_id: int = Path(..., title="User ID"),
    repo: Repository = Depends(get_users_repository),
):
    return services.update_user(repo, user_id, user.dict())


@app.delete("/users/{user_id}")
def delete_user(
    user_id: int = Path(..., title="User ID"),
    repo: Repository = Depends(get_users_repository),
):
    try:
        services.delete_user(repo, user_id)
    except services.UserNotFound:
        raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
