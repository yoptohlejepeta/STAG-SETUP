from fastapi import FastAPI, Request, Cookie
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def login(request: Request, stagUserTicket: str = None):
    login_url = os.getenv("LOGIN_URL")
    if stagUserTicket:
        return templates.TemplateResponse(
            "home.html", {"request": request, "ticket": stagUserTicket}
        )
    else:
        return templates.TemplateResponse(
            "login.html", {"request": request, "login_url": login_url}
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
