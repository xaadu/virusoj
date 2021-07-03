from fastapi import APIRouter, Response, Depends, status

from auth import AuthHandler

from models import (
    TestCase,
)
from db import (
    TestCaseDatabaseManager,
    ProblemDatabaseManager,
)

auth_handler = AuthHandler()
testcase_dm = TestCaseDatabaseManager.TestCaseDatabaseManager()
problem_dm = ProblemDatabaseManager.ProblemDatabaseManager()

router = APIRouter(
    prefix='/problems/{problem_id}/testcases',
    tags=['testcases'],
)


@router.get('/')
async def testcases(response: Response, problem_id: str, user: dict = Depends(auth_handler.allow_setter)):
    try:
        data = problem_dm.get_problem(problem_id)['data']
    except:
        pass

    if user['sub'] != data.get('creator') and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have enough permission.'
        }
    else:
        data = testcase_dm.get_testcases(problem_id=problem_id)
    return data


@router.post('/')
async def create_testcase(response: Response, problem_id: str, testcase: TestCase, user: dict = Depends(auth_handler.allow_setter)):
    try:
        data = problem_dm.get_problem(problem_id)['data']
    except:
        pass

    if user['sub'] != data.get('creator') and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have enough permission.'
        }
    else:
        data = testcase_dm.get_testcases(problem_id=problem_id)['data']
        if len(data) == 0:
            _id = 1
        else:
            _id = int(data[-1].get('_id'))+1

        testcase_data = dict(testcase)
        testcase_data['_id'] = _id

        data = testcase_dm.create_testcase(problem_id=problem_id, testcase_data=testcase_data)

    return data


@router.put('/{testcase_id}')
async def update_testcase(response: Response, problem_id: str, testcase_id: int, testcase: TestCase, user: dict = Depends(auth_handler.allow_setter)):

    try:
        data = problem_dm.get_problem(problem_id)['data']
    except:
        pass

    if user['sub'] != data.get('creator') and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have enough permission.'
        }
    else:
        testcase_data = dict(testcase)
        testcase_data['_id'] = testcase_id

        data = testcase_dm.update_testcase(problem_id=problem_id, testcase_data=testcase_data)

    return data


@router.delete('/{testcase_id}')
async def remove_testcase(response: Response, problem_id: str, testcase_id: int, user: dict = Depends(auth_handler.allow_setter)):

    try:
        data = problem_dm.get_problem(problem_id)['data']
    except:
        pass

    if user['sub'] != data.get('creator') and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have enough permission.'
        }
    else:
        data = testcase_dm.remove_testcase(problem_id=problem_id, testcase_id=testcase_id)

    return data
