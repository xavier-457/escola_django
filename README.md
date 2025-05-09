# 🏫 Sistema Escolar – Django + FastAPI

Este projeto é um sistema escolar desenvolvido com **Django** (para o sistema web) e **FastAPI** (para a API REST). 
Ele permite cadastrar e gerenciar alunos, professores, disciplinas e eventos tanto por uma interface web quanto por uma API moderna.

---

## 🔧 Tecnologias Usadas

- Python 3.10+
- Django 5.2
- Django REST Framework
- FastAPI
- HTML + CSS (estilização básica)
- SQLite3

---

## 📁 Estrutura do Projeto

escola_django/

├── cadastro/ # App Django com models, views, forms, templates

├── escola/ # Configurações principais do Django

├── fastapi_app/ # Projeto paralelo com FastAPI

├── templates/ # Templates HTML usados no Django

├── static/ # Arquivos de estilo CSS

├── db.sqlite3 # Banco de dados padrão

├── manage.py

└── README.md # Arquivo atual


---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

'''bash

**git clone https://github.com/seu-usuario/seu-repositorio.git**

**cd escola_django**


### **2. Criar ambiente virtual e ativar**

**python -m venv venv**

 Para Windows:
 
**venv\Scripts\activate**

 Para macOS/Linux:
 
**source venv/bin/activate**

### **3. Instalar as dependências**

**pip install -r requirements.txt**

Se não houver um arquivo requirements.txt, você pode criar com:

**pip freeze > requirements.txt**

### **4. Rodar o servidor Django**
   
**python manage.py migrate**

**python manage.py runserver**

Acesse o sistema pelo navegador:

Interface Admin: http://127.0.0.1:8000/admin

Formulários:

http://127.0.0.1:8000/cadastro/aluno

http://127.0.0.1:8000/cadastro/professor

http://127.0.0.1:8000/cadastro/disciplina

http://127.0.0.1:8000/cadastro/evento

## **🧪 Como Rodar a API FastAPI**
### **1. Navegue até a pasta da API:**

**cd fastapi_app**

### **2. Rode o servidor com Uvicorn:**

**uvicorn main:app --reload**

### **3. Acesse no navegador:**

Documentação Swagger: http://127.0.0.1:8000/docs

Documentação ReDoc: http://127.0.0.1:8000/redoc

## **✨ Funcionalidades**
Cadastro de Alunos, Professores, Disciplinas e Eventos

Visualização dos dados em listas organizadas

Interface administrativa (Django Admin)

Estilização com CSS (arquivo está em static/cadastro/style.css)

API REST usando FastAPI com endpoints de GET e POST

## **📝 Observações**
Os arquivos HTML utilizam herança de template com base.html.

Para carregar o CSS corretamente, o arquivo style.css precisa estar em:

**cadastro/static/cadastro/style.css**

No base.html, a linha de importação do CSS deve conter:

**{% load static %}**

**<link rel="stylesheet" href="{% static 'cadastro/style.css' %}"**

## **👤 Autor**
Desenvolvido por Matheus

📧 E-mail: matheussilxav33@gmail.com

🐙 GitHub: https://github.com/xavier-457
