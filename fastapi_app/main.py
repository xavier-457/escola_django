from fastapi import FastAPI
from models import Aluno, Professor, Disciplina, Evento
from data import alunos, professores, disciplinas, eventos

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "API da escola (FastAPI)"}

@app.get("/alunos/")
def listar_alunos():
    return alunos

@app.post("/alunos/")
def criar_aluno(aluno: Aluno):
    alunos.append(aluno)
    return aluno

@app.get("/professores/")
def listar_professores():
    return professores

@app.post("/professores/")
def criar_professor(professor: Professor):
    professores.append(professor)
    return professor

@app.get("/disciplinas/")
def listar_disciplinas():
    return disciplinas

@app.post("/disciplinas/")
def criar_disciplina(disciplina: Disciplina):
    disciplinas.append(disciplina)
    return disciplina

@app.get("/eventos/")
def listar_eventos():
    return eventos

@app.post("/eventos/")
def criar_evento(evento: Evento):
    eventos.append(evento)
    return evento
