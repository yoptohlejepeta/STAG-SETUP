from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from ..ticket import get_ticket

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/home", tags=["Home page"])


@router.get("/")
async def home_page(request: Request, ticket: str = Depends(get_ticket)):
    return templates.TemplateResponse(
        "home.html", {"request": request, "ticket": ticket}
    )
