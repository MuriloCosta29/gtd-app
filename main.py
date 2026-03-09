from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    # APIs retornam JSON, e JSON é estruturado como chave e valor.
    return {"status": "A API está rodando"}
