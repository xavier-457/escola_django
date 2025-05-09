from django.contrib import admin
from .models import (
    Curso,
    Professor,
    Aluno,
    Disciplina,
    Matricula,
    Departamento,
    Sala,
    Evento
)

admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Departamento)
admin.site.register(Sala)
admin.site.register(Evento)

