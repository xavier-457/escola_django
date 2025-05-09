from django.urls import path
from . import views
from .views import (
    AlunoAPIView, ProfessorAPIView,
    DisciplinaAPIView, EventoAPIView
)

urlpatterns = [
    path('aluno/', views.aluno_view, name='aluno'),
    path('professor/', views.professor_view, name='professor'),
    path('disciplina/', views.disciplina_view, name='disciplina'),
    path('evento/', views.evento_view, name='evento'),

    path('aluno/lista/', views.aluno_list, name='aluno_list'),
    path('professor/lista/', views.professor_list, name='professor_list'),
    path('disciplina/lista/', views.disciplina_list, name='disciplina_list'),
    path('evento/lista/', views.evento_list, name='evento_list'),

    path('api/alunos/', AlunoAPIView.as_view(), name='api-alunos'),
    path('api/professores/', ProfessorAPIView.as_view(), name='api-professores'),
    path('api/disciplinas/', DisciplinaAPIView.as_view(), name='api-disciplinas'),
    path('api/eventos/', EventoAPIView.as_view(), name='api-eventos'),

]
