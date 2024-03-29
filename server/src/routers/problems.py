from fastapi import APIRouter, Response, Depends, status

from typing import Optional

from auth import AuthHandler

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

auth_handler = AuthHandler()
problem_dm = ProblemDatabaseManager.ProblemDatabaseManager()

router = APIRouter(
    prefix='/problems',
    tags=['problems'],
)


@router.get('/')
async def problems(page: Optional[int] = 1, start: Optional[int] = None):
    if page < 1:
        page = 1
    if start is None:
        start = (page-1) * NUM_OF_DATA_PER_PAGE
        data = problem_dm.get_problems(NUM_OF_DATA_PER_PAGE, start)
    else:
        data = problem_dm.get_problems(page*NUM_OF_DATA_PER_PAGE, start)
    return data


@router.get('/filtered')
async def filtered_problems(response: Response, page: Optional[int] = 1, start: Optional[int] = None, user: dict = Depends(auth_handler.allow_setter)):
    if page < 1:
        page = 1

    if start is None:
        start = (page-1) * NUM_OF_DATA_PER_PAGE
        ndpp = NUM_OF_DATA_PER_PAGE
    else:
        ndpp = page*NUM_OF_DATA_PER_PAGE

    data = problem_dm.get_problems(ndpp, start, user['email'])

    if data['status'] == 'failed':
        response.status_code = status.HTTP_400_BAD_REQUEST

    return data


@router.post('/')
async def create_problem(problem: Problem, user: dict = Depends(auth_handler.auth_wrapper)):

    data = dict(problem)

    data['total_submission'] = 0
    data['accepted_submission'] = 0
    data['accepted_user_submission'] = 0
    data['creator_email'] = user['email']
    data['test_cases'] = list()

    data = problem_dm.create_problem(data)

    return data


@router.get('/{problem_id}')
async def get_problem(problem_id: str):

    data = problem_dm.get_problem(problem_id)

    return data


@router.put('/{problem_id}')
async def update_problem(response: Response, problem_id: str, problem: ProblemUpdate, user: dict = Depends(auth_handler.allow_setter)):

    try:
        data = problem_dm.get_problem(problem_id)['data']
    except:
        pass

    if user['email'] != data.get('creator_email') and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have permission to update this data'
        }
    else:
        problem = {k: v for k, v in dict(problem).items() if v is not None}
        data = problem_dm.update_problem(problem_id, problem)

    return data


@router.delete('/{problem_id}')
async def remove_problem(response: Response, problem_id: str, user: dict = Depends(auth_handler.allow_setter)):

    try:
        data = problem_dm.get_problem(problem_id)['data']
    except:
        pass

    if user['email'] != data.get('creator_email') and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have permission to delete this data'
        }
    else:
        data = problem_dm.remove_problem(problem_id)

    return data
