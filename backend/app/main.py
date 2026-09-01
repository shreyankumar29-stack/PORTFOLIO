from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="My Portfolio API",
    description="Personal portfolio powered by FastAPI",
    version="1.0.0"
)


# =========================================================
# STATIC FILES
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)


# =========================================================
# TEMPLATES
# =========================================================

templates = Jinja2Templates(
    directory="frontend/templates"
)


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# =========================================================
# ABOUT
# =========================================================

@app.get("/about")
def about(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="about.html"
    )


# =========================================================
# SKILLS
# =========================================================

@app.get("/skills")
def skills(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="skills.html"
    )


# =========================================================
# EDUCATION
# =========================================================

@app.get("/education")
def education(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="education.html"
    )


# =========================================================
# PROJECTS
# =========================================================

@app.get("/projects")
def projects(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="projects.html"
    )


# =========================================================
# PROJECT 1
# SMART CLASS ATTENDANCE CALCULATOR
# =========================================================

@app.get("/projects/attendance")
def attendance_project(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="attendance.html"
    )


# =========================================================
# PROJECT 2
# FACEMARK
# =========================================================

@app.get("/projects/facemark")
def facemark_project(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="facemark.html"
    )


# =========================================================
# CONTACT
# =========================================================

@app.get("/contact")
def contact(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="contact.html"
    )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }