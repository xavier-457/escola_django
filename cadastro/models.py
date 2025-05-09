from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Cursos"

    @property
    def nome_completo(self):
        return f"{self.codigo} - {self.nome}"

    @property
    def status(self):
        return "Ativo" if self.ativo else "Inativo"
    
    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Professores"

    @property
    def contato(self):
        return f"{self.nome} - {self.email}"

    @property
    def curso_nome(self):
        return self.curso.nome

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Alunos"

    @property
    def status(self):
        return "Ativo" if self.ativo else "Inativo"

    @property
    def curso_nome(self):
        return self.curso.nome
    
    def __str__(self):
        return self.nome



class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    obrigatoria = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Disciplinas"

    @property
    def nome_completo(self):
        return f"{self.codigo} - {self.nome}"

    @property
    def tipo(self):
        return "Obrigatória" if self.obrigatoria else "Optativa"
    
    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="matriculas")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data_matricula = models.DateField()
    nota_final = models.FloatField(null=True, blank=True)
    aprovado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Matrículas"

    @property
    def situacao(self):
        return "Aprovado" if self.aprovado else "Reprovado"

    @property
    def aluno_nome(self):
        return self.aluno.nome
    
    def __str__(self):
        return f"{self.aluno.nome} em {self.disciplina.nome}"


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    coordenador = models.OneToOneField(Professor, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Departamentos"

    @property
    def status(self):
        return "Ativo" if self.ativo else "Inativo"

    @property
    def coordenador_nome(self):
        return self.coordenador.nome if self.coordenador else "Sem coordenador"
    
    def __str__(self):
        return self.nome


class Sala(models.Model):
    numero = models.CharField(max_length=10)
    capacidade = models.IntegerField()
    bloco = models.CharField(max_length=10)
    ativa = models.BooleanField(default=True)
    curso = models.ManyToManyField(Curso)

    class Meta:
        verbose_name_plural = "Salas"

    @property
    def status(self):
        return "Disponível" if self.ativa else "Indisponível"

    @property
    def cursos_listados(self):
        return ", ".join([c.nome for c in self.curso.all()])
    
    def __str__(self):
        return f"Sala {self.numero} - Bloco {self.bloco}"


class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Eventos"

    @property
    def local(self):
        return f"Sala {self.sala.numero}" if self.sala else "Local não definido"

    @property
    def curso_nome(self):
        return self.curso.nome
    
    def __str__(self):
        return self.nome

