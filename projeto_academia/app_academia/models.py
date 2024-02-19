from django.db import models
from datetime import datetime

class Aluno(models.Model):
    CPF = models.BigIntegerField(primary_key=True) # dps a gente muda pra cpf
    nome_aluno = models.CharField(max_length=255)
    data_nasc = models.DateField()
    telefone = models.IntegerField()
    pacote = models.CharField(max_length = 14)

class Treino(models.Model):
    id_treino = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    treino = models.TextField(max_length=255)
    data_criacao = models.CharField(max_length=10, default=datetime.now().strftime('%d/%m/%Y'))
    exercicios = models.ManyToManyField('Exercicio')

class Exercicio(models.Model):
    nome_exercicio = models.CharField(max_length=255, primary_key=True)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
