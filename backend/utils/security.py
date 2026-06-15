import os
from argon2 import PasswordHasher
from functools import cache

ph = PasswordHasher()

# Hash the password
def hash_password(password: str) -> str:
    return ph.hash(password)

# Verify the password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return ph.verify(hashed_password, plain_password)
    except Exception:
        return False