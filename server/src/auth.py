from datetime import datetime, timedelta

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import jwt
from passlib.context import CryptContext


from env_vars import (
    SECRET_KEY,
    ALGORITHM,
)

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = SECRET_KEY
    algorithm = ALGORITHM

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id, email, role):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_id,
            'email': email,
            'role': role
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm=self.algorithm
        )

    def decode_token(self, token, roles: list = ['solver']):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[ALGORITHM])

            if payload['role'] not in roles:
                raise HTTPException(status_code=401, detail='You don\'t have enough permission for this request')
            
            del payload['exp']
            del payload['iat']
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)

    def allow_admin(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials, ['admin'])

    def allow_setter(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials, ['admin', 'setter'])

    def allow_solver(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials, ['admin', 'setter', 'solver'])
