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
BASE_DIR = Path(__file__).parent

connection = sqlite3.connect(BASE_DIR / "database" / "stores.db")

cursor = connection.cursor()

cursor.execute(table1)

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

    cursor.execute(cmd1, (store.store_name, store.location, str(uuid4())))

    cursor.execute("SELECT * FROM stores")

    stores = cursor.fetchall()

    connection.commit()
    connection.close()

    return {"success":True, "stores": stores}