from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base
# Column -> Tells sqlalchemy "This is a database column" |
# Integer, String and DateTime -> Tell the data type of each column.
# func -> Gives access to SQL functions. `func.now()` calls the database's built-in functions to get the current timestamp automatically.


class InboxItemModel(Base):  # Represent the database table
    __tablename__ = "inbox"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    created_at = Column(DateTime, server_default=func.now())
