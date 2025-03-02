from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


# from_attributes =True — позволяет создавать объект модели напрямую из атрибутов Python-объектов (например,
# когда поля модели совпадают с атрибутами другого объекта). Чаще всего опция применяется для преобразования
# моделей ORM к моделям Pydantic.

class STaskId(BaseModel):
    task_id: int
