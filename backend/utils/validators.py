import re


EMAIL_REGEX = re.compile(
    r"^[^@]+@[^@]+\.[^@]+$"
)


def is_valid_email(
    email: str,
) -> bool:
    return bool(
        EMAIL_REGEX.match(email)
    )


PHONE_REGEX = re.compile(
    r"^[6-9]\d{9}$"
)


def is_valid_phone(
    phone: str,
) -> bool:
    return bool(
        PHONE_REGEX.match(phone)
    )