from linecache import cache
import os
from argon2 import PasswordHasher

#lazy initializing the variable
@cache
def get_password_hasher() -> PasswordHasher:
    return PasswordHasher()

# Hash the password
def hash_password(password: str) -> str:
    return get_password_hasher.hash(password)

# Verify the password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return get_password_hasher.verify(hashed_password, plain_password)
    except Exception:
        return False