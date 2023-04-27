from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


@app.get("/{path:path}")
def redirect(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)], path: str
):
    return RedirectResponse(
        f"https://dl.fontawesome.com/{credentials.password}/fontawesome-pro/python/simple/{path}"
    )
