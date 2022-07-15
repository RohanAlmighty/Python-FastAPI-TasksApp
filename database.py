from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env import sqlite_url, postgresql_url

# For SQLLite
"""
SQLALCHEMY_DATABASE_URL = sqlite_url
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
"""

# For PostgreSQL
SQLALCHEMY_DATABASE_URL = postgresql_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
