# responsible for connecting to the database.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# ---------------------------------------------------------------------------------------------------

engine = create_engine(
    "sqlite:///database.db", connect_args={"check_same_thread": False}
)
# When i run the project, sqlalchemy create a file called database.db in my project folder automatically.
# `check_same_thread: False`: allow multiple threads (FastAPI workers)
# To use the same database connection simultaneously.

# ---------------------------------------------------------------------------------------------------


class Base(DeclarativeBase):
    pass


# Base is the parent of all my database models. When i go to create the table for `InboxItem` later, she will inherit from class `Base`. That's how sqlalchemy knows it's a database not a normal class from python.
# Recap: The sqlalchemy knows if a class is a database or not looking if the class have a parent how is a database.

# ---------------------------------------------------------------------------------------------------

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# im correct! autocommit is for not save automatically. autoflush -> Means sqlalchemy won't send queries to the database before i'm ready.

# ---------------------------------------------------------------------------------------------------


def get_session():
    db = SessionLocal()
    try:
        yield db  # yield -> is what makes FastAPI inject the session into my routes automatically.
    finally:  # finally -> guarantees the session closes even if something goes wrong.
        db.close()
