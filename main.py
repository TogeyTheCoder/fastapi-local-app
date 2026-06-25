from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Access app in http://127.0.0.1:8000
# Root is still http://0.0.0.0:8000
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request, "backend_msg":"Hello from FastAPI!"}
    )