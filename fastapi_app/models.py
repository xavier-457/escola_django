from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    matricula: str
    email: str
    curso: str

class Professor(BaseModel):
    nome: str
    matricula: str
    email: str

class Disciplina(BaseModel):
    nome: str
    codigo: str
    carga_horaria: int
    curso: str

class Evento(BaseModel):
    nome: str
    data: str  # Use string no formato "YYYY-MM-DD"
    descricao: str
    curso: str

