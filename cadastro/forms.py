from django import forms
from .models import Aluno, Professor, Disciplina, Evento

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
