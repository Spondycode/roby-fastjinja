from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from dogs import DOGS

# from routes.route import router

# name = "David"

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "name": "Fast Jinja Home"}
    )


@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "name": "Fast Jinja About", "dogs": DOGS}
    )


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        "login.html", {"request": request, "name": "Fast Jinja Login"}
    )


# app.include_router(router)
