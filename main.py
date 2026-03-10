from fastapi import FastAPI, Depends

# Depends tell to FastAPI "before running this route, inject this dependency as a parameter."
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_session
from models import InboxItemModel
from models import Base
from database import engine
# when i call get_db inside de function, FastAPI doens't know it's a dependecy -- it's just a function call that does nothing useful there.

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "A api está funcionando corretamente."}


class InboxItem(BaseModel):  # Validates what arrives in the request
    text: str


# ------------------------------------------------------------------------------------------------------------
# NOTE: I can't add a class!!! I have to create de instance first and after this call the instance
# db.add() -> adds the object to the session
# db.commit() -> Saves to the database
# db.refresh -> updates the object with data from the database
@app.post("/inbox")
def make_inbox_item(
    item: InboxItem, db: Session = Depends(get_session)
):  # now db is my database session
    new_task = InboxItemModel(text=item.text)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"item": "inbox adicionado com sucesso.", "texto": item.text}


# ------------------------------------------------------------------------------------------------------------
# For GET i don't need commit() and refresh()
@app.get("/inbox")
def return_inbox(db: Session = Depends(get_session)):
    tasks = db.query(InboxItemModel).all()  # Save result in a variable
    return {"inbox": tasks}  # Return the variable with result.
