from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
from uuid import uuid4
import sqlite3

from .tables import *

class Store(BaseModel):
    location: str
    store_name: str

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
APP_DIR = Path(__file__).parent
ROOT_DIR = Path(APP_DIR).parent

# Access app in http://127.0.0.1:8000
# Root is still http://0.0.0.0:8000
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request, "backend_msg":"Hello from FastAPI!"}
    )

@app.post("/stores/")
async def execute_tables(store: Store):

    connection = sqlite3.connect(ROOT_DIR / "database" / "stores.db")
    cursor = connection.cursor()
    cursor.execute(table1)

    cursor.execute(cmd1, (store.store_name, store.location, str(uuid4())))

    connection.commit()
    connection.close()

    return {"success":True}

@app.get("/stores/fetch_all/")
async def fetch_all_stores():
    
    connection = sqlite3.connect(ROOT_DIR / "database" / "stores.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM stores")

    stores = cursor.fetchall()

    connection.close()
    return {"success": True, "stores": stores}