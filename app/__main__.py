from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os

from routers import home

load_dotenv()
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.exception_handler(404)
async def handler_404(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request})


@app.get("/")
def login(request: Request, stagUserTicket: str = None):
    login_url = os.getenv("LOGIN_URL")
    if stagUserTicket:
        return RedirectResponse(url=f"/home/?stagUserTicket={stagUserTicket}")
    else:
        return templates.TemplateResponse(
            "login.html", {"request": request, "login_url": login_url}
        )


app.include_router(home.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
