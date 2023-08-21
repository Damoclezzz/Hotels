from fastapi import HTTPException, status


class TokenException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token validation error'

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TokenValidationException(TokenException):
    detail = 'Token is not valid'


class TokenExpiredException(TokenException):
    detail = 'Token is expired'


class TokenSubKeyNotExists(TokenException):
    detail = 'Token has no "sub" key parameter'
