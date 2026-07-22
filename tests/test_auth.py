from backend.authentication.password import (
    hash_password,
    verify_password,
)

hashed = hash_password("Admin@123")

print(
    verify_password(
        "WrongPassword",
        hashed
    )
)