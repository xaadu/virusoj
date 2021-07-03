import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


DEBUG=os.environ.get('DEBUG', 'TRUE') == 'TRUE'
if DEBUG:
    import dotenv
    dotenv.load_dotenv('../.env')


from routers import (
    problems,
    testcases,
    auth,
    users,
)


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
app.include_router(testcases.router)
app.include_router(auth.router)
app.include_router(users.router)
