from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(
    title="My Portfolio API",
    description="Personal portfolio powered by FastAPI",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)


templates = Jinja2Templates(directory="frontend/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
def health_check():
    return {"status": "healthy"}