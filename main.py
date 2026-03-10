from fastapi import FastAPI
from pydantic import BaseModel

inbox = []

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "A api está funcionando corretamente."}


class InboxItem(BaseModel):  # Validates what arrives in the request
    text: str


@app.post("/inbox")
def make_inbox_item(item: InboxItem):
    inbox.append(item.text)
    return {"item": "inbox adicionado com sucesso.", "texto": item.text}


@app.get("/inbox")
def return_inbox():
    return {"inbox": inbox}
