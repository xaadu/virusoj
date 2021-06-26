from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import helpers

from routers import problems

APP_VERSION = '1'

ROOT_PATH = f'/virusoj/v{APP_VERSION}'

app = FastAPI(
    title="Virus Online Judge API",
    description="This is a small API Project For Virus Online Judge",
    version=APP_VERSION+'.0'
)
app.mount(ROOT_PATH, app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    return {'status': 'success', 'data': 'Virus Online Judge'}


app.include_router(problems.router)
