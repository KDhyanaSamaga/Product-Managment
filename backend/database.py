from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from typing import Generator

import os

# 1. Fallback for local development if env variable isn't set
DB_URL = os.getenv("DATABASE_URL")

# 2. Performance tuning for scalability
engine = create_engine(
    DB_URL,
    pool_size=20,          # Keeps up to 20 persistent connections open
    max_overflow=10,       # Allows up to 10 extra connections during peak traffic
    pool_timeout=30,       # Seconds to wait before throwing a timeout error
    pool_recycle=1800,     # Recycles connections every 30 mins to prevent stale links
    )
# 3. Session factory (using lowercase naming convention to avoid class confusion)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush= False,
    bind=engine
)
# 4. Modern declarative base declaration
Base = declarative_base()

def get_db() -> Generator[Session,None,None]:
    # Creates a new database session for each request.
    # This ensures that concurrent requests use separate sessions,
    # preventing conflicts and maintaining proper database connection management.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


        