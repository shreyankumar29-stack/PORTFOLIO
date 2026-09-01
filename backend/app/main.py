from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


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
# CONTACT - GET
# =========================================================

@app.get("/contact")
def contact(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="contact.html"
    )


# =========================================================
# CONTACT - POST
# =========================================================

@app.post("/contact")
def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):

    try:

        # -------------------------------------------------
        # CREATE EMAIL
        # -------------------------------------------------

        email_message = EmailMessage()

        email_message["From"] = EMAIL_ADDRESS
        email_message["To"] = EMAIL_ADDRESS
        email_message["Reply-To"] = email

        email_message["Subject"] = (
            f"Portfolio Contact: {subject}"
        )

        email_message.set_content(
            f"""
You have received a new message from your portfolio website.

Name:
{name}

Email:
{email}

Subject:
{subject}

Message:
{message}
"""
        )


        # -------------------------------------------------
        # SEND EMAIL THROUGH GMAIL SMTP
        # -------------------------------------------------

        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as smtp:

            smtp.starttls()

            smtp.login(
                EMAIL_ADDRESS,
                EMAIL_APP_PASSWORD
            )

            smtp.send_message(
                email_message
            )


        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context={
                "success": True,
                "message": (
                    "Your message has been sent successfully!"
                )
            }
        )


    except Exception as error:

        print("EMAIL ERROR:")
        print(error)


        # -------------------------------------------------
        # ERROR
        # -------------------------------------------------

        return templates.TemplateResponse(
            request=request,
            name="contact.html",
            context={
                "success": False,
                "message": (
                    "Something went wrong. "
                    "Please try again later."
                )
            }
        )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }