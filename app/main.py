from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import redis

from .routers import home
from .settings import Settings
from .ticket import get_ticket


settings = Settings()
r = redis.Redis(
    host=settings.redis.host, port=settings.redis.port, db=settings.redis.db
)
app = FastAPI(
    
    docs_url=None,
    redoc_url=None,
)
templates = Jinja2Templates(directory="app/templates")


@app.exception_handler(404)
async def handler_404(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request})

@app.exception_handler(401)
async def handler_401(request: Request, exc: HTTPException):
    login_url = settings.app.login_url
    return templates.TemplateResponse("401.html", {"request": request, "login_url": login_url})


@app.get("/")
def login(request: Request, stagUserTicket: str | None = None):
    login_url = settings.app.login_url
    if stagUserTicket:
        r.setex("stagUserTicket", 1800, stagUserTicket)
        return RedirectResponse(url=f"/home")
    else:
        return templates.TemplateResponse(
            "login.html", {"request": request, "login_url": login_url}
        )


app.include_router(home.router)
