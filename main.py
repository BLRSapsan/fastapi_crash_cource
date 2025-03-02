import uvicorn
import create_fastapi
from router import router as tasks_router

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

app = create_fastapi.create_app(create_custom_static_urls=True)
app.include_router(tasks_router)
