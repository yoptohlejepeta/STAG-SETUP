from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/favicon.ico")
# async def icon():
#     return FileResponse("static/stag_favcon.ico")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
