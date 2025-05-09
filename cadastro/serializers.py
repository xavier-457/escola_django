from rest_framework import serializers
from .models import Aluno, Professor, Disciplina, Evento

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

