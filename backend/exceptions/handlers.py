from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from backend.exceptions.custom_exceptions import (
    DuplicateResourceException,
    ForbiddenException,
    ResourceNotFoundException,
    UnauthorizedException,
    ValidationException,
)
from backend.exceptions.error_codes import ErrorCode


def register_exception_handlers(
    app: FastAPI,
):

    @app.exception_handler(
        ResourceNotFoundException
    )
    async def resource_not_found(
        request: Request,
        exc: ResourceNotFoundException,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "error": {
                    "code": ErrorCode.RESOURCE_NOT_FOUND,
                    "message": exc.message,
                },
            },
        )

    @app.exception_handler(
        DuplicateResourceException
    )
    async def duplicate_resource(
        request: Request,
        exc: DuplicateResourceException,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "error": {
                    "code": ErrorCode.DUPLICATE_RESOURCE,
                    "message": exc.message,
                },
            },
        )

    @app.exception_handler(
        ValidationException
    )
    async def validation_error(
        request: Request,
        exc: ValidationException,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "error": {
                    "code": ErrorCode.VALIDATION_ERROR,
                    "message": exc.message,
                },
            },
        )

    @app.exception_handler(
        UnauthorizedException
    )
    async def unauthorized(
        request: Request,
        exc: UnauthorizedException,
    ):
        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "error": {
                    "code": ErrorCode.UNAUTHORIZED,
                    "message": exc.message,
                },
            },
        )

    @app.exception_handler(
        ForbiddenException
    )
    async def forbidden(
        request: Request,
        exc: ForbiddenException,
    ):
        return JSONResponse(
            status_code=403,
            content={
                "success": False,
                "error": {
                    "code": ErrorCode.FORBIDDEN,
                    "message": exc.message,
                },
            },
        )