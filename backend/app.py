import os 
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse


app = FastAPI()


ROOT_PATH = os.path.join(os.path.dirname(__file__), "..")
public_file_abspath = os.path.join(ROOT_PATH, "public")

app.mount("/", StaticFiles(directory=public_file_abspath), name="public")


@app.get("/api")
def index():
    return JSONResponse({"status": 200, "msg": "ok"})



