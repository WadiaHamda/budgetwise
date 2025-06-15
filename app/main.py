from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import router

app = FastAPI()
app.include_router(router)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")