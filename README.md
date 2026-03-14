# GTD App

## Por que eu criei isso?

Há alguns meses comecei a usar o método GTD (Getting Things Done) para organizar minha vida pessoal e acadêmica. Usava o notion para isso, mas o Notion é amplo demais -- me dispersava com recursos que não precisava.

Decidi construir minha própria ferramenta: Focada exclusivamente no GTD, sem distrações e com uma interface limpa pensada para produtividade real.

## O que é o GTD?

GTD é um método de produtividade criado por David Allen baseado em capturar tudo que ocupa sua mente, processar cada item com perguntas objetivas e organizar em listas de ação concretas.

## Tecnologias
- Python + FastAPI
- SQLite
- Docker

## Status
🚧 Em desenvolvimento

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Status da API |
| POST | /inbox | Cria uma nova tarefa na inbox |
| GET | /inbox | Retorna todas as tarefas da inbox |

## Roadmap

### Backend
- [x] Health check endpoint
- [x] `POST /inbox` — captura tarefas
- [x] `GET /inbox` — retorna tarefas
- [x] Banco de dados SQLite
- [x] `DELETE /inbox/{id}` — remover tarefa processada
- [ ] `PATCH /inbox/{id}` — atualizar status de uma tarefa

### Frontend
- [ ] Interface

### DevOps
- [ ] Conteinerização com Docker
