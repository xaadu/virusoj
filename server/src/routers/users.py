from typing import Optional
from fastapi import APIRouter, Response, status, Depends
from auth import AuthHandler

from db.UserDatabaseManager import UserDatabaseManager

from env_vars import (
    NUM_OF_DATA_PER_PAGE,
)
from models import (
    UserUpdate
)

auth_handler = AuthHandler()
user_dm = UserDatabaseManager()


router = APIRouter(
    prefix='/users',
    tags=['Users'],
    dependencies=[
        Depends(auth_handler.allow_solver),
    ]
)


@router.get('/', dependencies=[Depends(auth_handler.allow_admin)])
async def users(response: Response, page: Optional[int] = 1, start: Optional[int] = None):
    if page < 1:
        page = 1
    if start is None:
        start = (page-1) * NUM_OF_DATA_PER_PAGE
        data = user_dm.get_users(NUM_OF_DATA_PER_PAGE, start)
    else:
        data = user_dm.get_users(page*NUM_OF_DATA_PER_PAGE, start)

    if data['status'] == 'failed':
        response.status_code = status.HTTP_400_BAD_REQUEST

    return data


@router.get('/{user_id}')
async def get_user(user_id: str, response: Response):

    data = user_dm.get_user(user_id)

    if data['status'] == 'failed':
        response.status_code = status.HTTP_400_BAD_REQUEST

    return data


@router.put('/{user_id}')
async def update_user(user_id: str, user_data: UserUpdate, response: Response, user: dict = Depends(auth_handler.auth_wrapper)):

    if user['sub'] != user_id and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have permission to update this data'
        }
    else:
        # Only Admin can Change Role
        if user['role'] != 'admin':
            del user_data.role

        user_data = {k: v for k, v in dict(user_data).items() if v is not None}
        data = user_dm.update_user(user_id=user_id, user_data=user_data)

        if data['status'] == 'failed':
            response.status_code = status.HTTP_400_BAD_REQUEST

    return data


@router.delete('/{user_id}')
async def delete_user(user_id: str, response: Response, user: dict = Depends(auth_handler.auth_wrapper)):

    if user['sub'] != user_id and user['role'] != 'admin':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        data = {
            'status': 'failed',
            'reason': 'You don\'t have permission to delete this data'
        }
    else:
        data = user_dm.remove_user(user_id=user_id)

        if data['status'] == 'failed':
            response.status_code = status.HTTP_400_BAD_REQUEST

    return data
