from fastapi import FastAPI
from pydantic import BaseModel

inbox = []

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "A api está funcionando corretamente."}


class InboxItem(BaseModel):
    text: str


@app.post("/inbox")
def cria_inbox_item(item: InboxItem):
    inbox.append(item.text)
    return {"item": "inbox adicionado com sucesso.", "texto": item.text}


@app.get("/inbox")
def retorna_inbox():
    return {"inbox": inbox}
