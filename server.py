#!/usr/bin/env python

import uvicorn

from fastapi import Depends, Request, FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from contextlib import asynccontextmanager

from routers import BASE_PATH, config, resource, schema, users, groups
from utils.auth import api_key_auth
from utils import host, port

import os
import logging

level = logging.INFO \
    if os.environ.get('LOGLEVEL', 'INFO') == 'INFO' else logging.ERROR
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Why is this here in the first place?
    pass
    yield
    pass

app = FastAPI(lifespan=lifespan)

app = FastAPI(
    lifespan=lifespan,
    title="SCIM Sample",
    docs_url=BASE_PATH if BASE_PATH.startswith('/') else '/',
    redoc_url=None,
    dependencies=[Depends(api_key_auth)],
    openapi_url=BASE_PATH + '/openapi.json',
    responses={
        401: {"description": "Operation forbidden"},
        404: {"description": "Not found"},
        422: {"description": "Unprocessable input"},
    },
)

app.include_router(config.router)
app.include_router(resource.router)
app.include_router(schema.router)
app.include_router(users.router)
app.include_router(groups.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    logging.error(f"{request}: {exc_str}")
    content = {'status_code': 10422, 'message': exc_str}
    return JSONResponse(
        content=content,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
