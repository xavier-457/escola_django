from django.shortcuts import render
from .forms import AlunoForm, ProfessorForm, DisciplinaForm, EventoForm
from .models import Aluno, Professor, Disciplina, Evento
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlunoSerializer, ProfessorSerializer, DisciplinaSerializer, EventoSerializer

def aluno_view(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno salvo com sucesso!')
    else:
        form = AlunoForm()

    return render(request, 'cadastro/form_aluno.html', {'form': form})

def professor_view(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor salvo com sucesso!')
    else:
        form = ProfessorForm()
    return render(request, 'cadastro/form_professor.html', {'form': form})

def disciplina_view(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disciplina salva com sucesso!')
    else:
        form = DisciplinaForm()
    return render(request, 'cadastro/form_disciplina.html', {'form': form})

def evento_view(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento salvo com sucesso!')
    else:
        form = EventoForm()
    return render(request, 'cadastro/form_evento.html', {'form': form})

def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'cadastro/list_aluno.html', {'alunos': alunos})


def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'cadastro/list_professor.html', {'professores': professores})


def disciplina_list(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'cadastro/list_disciplina.html', {'disciplinas': disciplinas})


def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'cadastro/list_evento.html', {'eventos': eventos})

class AlunoAPIView(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorAPIView(APIView):
    def get(self, request):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaAPIView(APIView):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventoAPIView(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


