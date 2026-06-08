import os
from typing import Optional,Dict,Any
from datetime import datetime, timedelta, timezone


# From the .env file dont mention this anywhere
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')


def create_access_token(data:Dict[str, Any], expires_delta: Optional[timedelta] = None):