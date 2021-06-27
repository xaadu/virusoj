from fastapi import APIRouter, Request

from models import (
    TestCase,
)
from db.TestCaseDatabaseManager import TestCaseDatabaseManager

router = APIRouter(
    prefix='/problems/{problem_id}/testcases',
    tags=['testcases'],
)


testcase_dm = TestCaseDatabaseManager()


@router.get('/')
async def testcases(request: Request, problem_id: str):
        data = testcase_dm.get_testcases(problem_id=problem_id)
        return data


@router.post('/')
async def create_testcase(request: Request, problem_id: str, testcase: TestCase):
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
async def update_testcase(request: Request, problem_id: str, testcase_id: int, testcase: TestCase):

    testcase_data = dict(testcase)
    testcase_data['_id'] = testcase_id

    data = testcase_dm.update_testcase(problem_id=problem_id, testcase_data=testcase_data)

    return data


@router.delete('/{testcase_id}')
async def remove_testcase(request: Request, problem_id: str, testcase_id: int):

    data = testcase_dm.remove_testcase(problem_id=problem_id, testcase_id=testcase_id)

    return data
