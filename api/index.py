from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


@app.get("/")
def index():
    return RedirectResponse("https://github.com/celsiusnarhwal/foxy")


@app.get("/simple/{path:path}")
def repository(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)], path: str
):
    return RedirectResponse(
        f"https://dl.fontawesome.com/{credentials.password}/fontawesome-pro/python/simple/{path}"
    )
