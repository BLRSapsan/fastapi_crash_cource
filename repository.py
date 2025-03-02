from sqlalchemy import select

from database import new_session, TasksOrm
from schemas import STaskAdd, STask


class TasksRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()  # создать словарь из аргументов
            task = TasksOrm(**task_dict) #создает новую строку,
            # но пока хранит ее только внутри нашего FastAPI приложения — база данных еще ничего не знает про нее.
            session.add(task) #добавить новую строку в объект сессии, чтобы SQLAlchemy знала, какие изменения
            # нужно будет отправлять в базу данных, однако по-прежнему мы ничего не сообщили базе данных о новой задаче.
            await session.flush()  # отправить изменения в базу, получить обратно id
            await session.commit()  # сохранить изменения в базе
            return task.id

    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks
