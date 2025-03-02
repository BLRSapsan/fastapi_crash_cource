from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TasksRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TasksRepository.add_one(task)
    return {"task_id": task_id}


@router.get("")
async def get_task() -> list[STask]:
    tasks = await TasksRepository.get_tasks()
    return tasks
