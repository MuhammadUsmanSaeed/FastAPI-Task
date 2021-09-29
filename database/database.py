from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from contextlib import contextmanager
from setting import config

SQLALCHEMY_DATABASE_URL = f"mysql://{config.DATABASE_CONFIG['MYSQL_USERNAME']}:" \
                          f"{config.DATABASE_CONFIG['MySQL_PASSWORD']}@" \
                          f"{config.DATABASE_CONFIG['MYSQL_HOST']}/{config.DATABASE_CONFIG['MYSQL_DATABASE']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# @contextmanager
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
