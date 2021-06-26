from fastapi import APIRouter, Request

from typing import Optional

from env_vars import (
    NUM_OF_DATA_PER_PAGE,
)

from models import (
    Problem,
    ProblemUpdate,
)
from db import (
    ProblemDatabaseManager
)

router = APIRouter(
    prefix='/problems',
    tags=['problems'],
)


problem_dm = ProblemDatabaseManager.ProblemDatabaseManager()


@router.get('/')
async def problems(request: Request, page: Optional[int] = 1, start: Optional[int] = None):
    if page < 1:
        page = 1
    if start is None:
        start = (page-1) * NUM_OF_DATA_PER_PAGE
        data = problem_dm.get_problems(NUM_OF_DATA_PER_PAGE, start)
    else:
        data = problem_dm.get_problems(page*NUM_OF_DATA_PER_PAGE, start)
    return data


@router.post('/')
async def create_problem(request: Request, problem: Problem):

    data = dict(problem)

    data['total_submission'] = 0
    data['accepted_submission'] = 0
    data['accepted_user_submission'] = 0

    data = problem_dm.create_problem(data)

    return data


@router.get('/{problem_id}')
async def get_problem(request: Request, problem_id: str):

    data = problem_dm.get_problem(problem_id)

    return data


@router.put('/{problem_id}')
async def update_problem(request: Request, problem_id: str, problem: ProblemUpdate):

    problem = {k: v for k, v in dict(problem).items() if v is not None}

    data = problem_dm.update_problem(problem_id, problem)

    return data


@router.delete('/{problem_id}')
async def remove_problem(request: Request, problem_id: str):

    data = problem_dm.remove_problem(problem_id)

    return data
