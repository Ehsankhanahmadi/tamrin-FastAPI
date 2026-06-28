from fastapi import FastAPI, responses
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", responses=HTMLResponse)
async def home(req) -> str:
    return templates.TemplateResponse(request=req,name="index.html",context={})


# if __name__ == "__main__":
    # uvicorn.run("app/main:app",host="127.0.0.1",port=8000, reload=True)