from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from functools import lru_cache
from fastapi import Depends, FastAPI

from core import config
from core.log import logger
from crud import quote as quoteCRUD

logger.info("Starting App")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/", response_class=HTMLResponse)
async def get_quote(
    request: Request, settings: config.Settings = Depends(get_settings)
):
    quote = quoteCRUD.get_quote_simple(url=settings.url_quote_backend)
    logger.debug("Message Recieved: " + str(quote))
    return templates.TemplateResponse(
        "index.html", {"request": request, "quote": quote}
    )
