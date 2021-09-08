from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting import config

SQLALCHEMY_DATABASE_URL = f"mysql://{config.DATABASE_CONFIG['user']}:{config.DATABASE_CONFIG['password']}@" \
                          f"{config.DATABASE_CONFIG['host']}/{config.DATABASE_CONFIG['dbname']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
