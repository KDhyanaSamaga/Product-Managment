"""
Use this only once if used then change the secret key
from the .env file its compulsory and make sure not to run this file
and also dont use this file anywhere
"""

import secrets

print(secrets.token_hex(32))  # 256-bit key