from fastapi import HTTPException, status


class CredentialsException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Wrong credentials'

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class AccountAlreadyExistsException(CredentialsException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Account with this email already exists'


class IncorrectLoginOrPasswordException(CredentialsException):
    detail = 'Incorrect login or password'


class AccountNotExistsException(CredentialsException):
    detail = 'Account with this email does not exists'
