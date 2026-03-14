# API | Routes | Schemas | Applications instance.

# ------------------------------------------------------------------------------------------------

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
)  # Depends() -> what have inside parantheses, the FastAPI call and say: "before running this route, call what's inside () and inject the result as db(example.)"

from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_session
from models import InboxItemModel
from models import Base
from database import engine

# ------------------------------------------------------------------------------------------------

Base.metadata.create_all(bind=engine)  # Creates the table in the database file.
app = FastAPI()

# ------------------------------------------------------------------------------------------------


@app.get("/")
def health_check():
    return {
        "status": "A api está funcionando corretamente."
    }  # Check if API is working.


# ------------------------------------------------------------------------------------------------


class InboxItem(BaseModel):  # Validates what arrives in the request
    text: str


# ------------------------------------------------------------------------------------------------


@app.post("/inbox")
def make_inbox_item(
    item: InboxItem, db: Session = Depends(get_session)
):  # now db is my database session
    new_task = InboxItemModel(text=item.text)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"item": "inbox adicionado com sucesso.", "texto": item.text}


# ------------------------------------------------------------------------------------------------


# GET i don't need commit() and refresh()
@app.get("/inbox")
def return_inbox(db: Session = Depends(get_session)):
    tasks = db.query(InboxItemModel).all()  # Save result in a variable
    return {"inbox": tasks}  # Return the variable with result.


# ------------------------------------------------------------------------------------------------

# .all() -> return the entire list
# .first() -> Return only the first item of that list -- or `None` if nothing was found. For delete by id i only need one specific task.


@app.delete("/inbox/{id}")
def delete_task(id: int, db: Session = Depends(get_session)):
    task_del = db.query(InboxItemModel).filter(InboxItemModel.id == id).first()
    if task_del is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task_del)
    db.commit()
    return {"message": "Tarefa deletada com sucesso", "id": id}


# ------------------------------------------------------------------------------------------------


@app.patch("/inbox/{id}")
def edit_task(id: int, change: InboxItem, db: Session = Depends(get_session)):
    task = db.query(InboxItemModel).filter(InboxItemModel.id == id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    task.text = change.text
    db.commit()
    db.refresh(task)
    return task
