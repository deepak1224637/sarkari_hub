from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Mount static files (if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates (if you want to render HTML)
templates = Jinja2Templates(directory="accounts/templates")

@app.get("/fastapi-login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/fastapi-login", response_class=HTMLResponse)
def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    # Dummy authentication logic (replace with real user check)
    if username == "admin" and password == "admin":
        message = "Login successful!"
    else:
        message = "Invalid username or password."
    return templates.TemplateResponse("login.html", {"request": request, "message": message})
