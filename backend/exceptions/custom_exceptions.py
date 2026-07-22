class TalentFlowException(Exception):
    """Base exception for TalentFlow AI."""

    def __init__(
        self,
        message: str,
    ):
        self.message = message
        super().__init__(message)


class ResourceNotFoundException(
    TalentFlowException
):
    pass


class DuplicateResourceException(
    TalentFlowException
):
    pass


class ValidationException(
    TalentFlowException
):
    pass


class UnauthorizedException(
    TalentFlowException
):
    pass


class ForbiddenException(
    TalentFlowException
):
    pass