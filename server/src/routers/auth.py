from fastapi import APIRouter, Response, status
from auth import AuthHandler

from models import (
    UserLogin,
    UserRegister
)
from db.UserDatabaseManager import UserDatabaseManager

router = APIRouter(
    prefix='/auth',
    tags=['authentication'],
)

auth_handler = AuthHandler()
user_dm = UserDatabaseManager()

@router.post('/register')
def register(user_details: UserRegister, response: Response):
    users = user_dm.get_users()['data']
    if any(x['email'] == user_details.email for x in users):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 'failed', 'reason': 'Email is being used.'}
    hashed_password = auth_handler.get_password_hash(user_details.password)
    user_details.password = hashed_password

    data = dict(user_details)
    data['password'] = hashed_password
    data['role'] = 'solver'
    data['total_submission'] = 0
    data['accepted_submission'] = 0

    data = user_dm.create_user(data)

    data['token'] =  auth_handler.encode_token(data['data']['_id'], data['data']['email'], data['data']['role'])

    return data



@router.post('/login')
def login(user_details: UserLogin, response: Response):
    user = None
    users = user_dm.get_users()['data']
    for x in users:
        if x['email'] == user_details.email:
            data = user_dm.get_user(x['email'])
            if data['status']=='success':
                user = data['data']
                break
            else:
                return data

    print(user)
    if (user is None) or (not auth_handler.verify_password(user_details.password, user['password'])):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {'status': 'failed', 'reason': 'Invalid Username / Password'}

    token = auth_handler.encode_token(user['_id'], user['email'], user['role'])

    data = {
        '_id': user['_id'],
        'email': user['email'],
        'role': user['role']
    }

    return { 'status': 'success', 'token': token, 'data': data }
