from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/home", tags=["Home page"])


@router.get("/")
async def home(request: Request, stagUserTicket: str):
    return templates.TemplateResponse(
        "home.html", {"request": request, "ticket": stagUserTicket}
    )
