from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# =========================================================
# APP
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
# CONTACT PAGE
# =========================================================

@app.get("/contact")
def contact(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="contact.html"
    )


# =========================================================
# CONTACT FORM
# =========================================================

@app.post("/contact")
def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):

    return {
        "success": True,
        "message": "Your message has been received!",
        "data": {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }