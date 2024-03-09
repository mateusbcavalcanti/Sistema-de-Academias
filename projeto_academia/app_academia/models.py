from django.db import models
from datetime import datetime


class Aluno(models.Model):
    cpf = models.TextField(primary_key=True, default=0)
    nome = models.CharField(max_length=255)
    data_nasc = models.DateField(null=True)
    telefone = models.IntegerField()
    pacote = models.CharField(max_length=14)


class Treino(models.Model):
    id_treino = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    treino = models.TextField(max_length=255)
    data_criacao = models.CharField(
        max_length=10, default=datetime.now().strftime('%d/%m/%Y'))
    exercicios = models.ManyToManyField('Exercicio')


class Exercicio(models.Model):
    nome_exercicio = models.CharField(max_length=255, primary_key=True)
    series = models.IntegerField()
    repeticoes = models.IntegerField()

class Funcionario(models.Model):
    cpf = models.TextField(max_length=255, primary_key=True)
    nome = models.TextField(max_length=255)
    telefone = models.IntegerField()
    endereco = models.TextField(max_length=255)
    data_admissao = models.DateField()
    salario = models.IntegerField()

class Unidade(models.Model):
    nome = models.TextField(max_length=255, primary_key=True)
    endereco = models.TextField(max_length=255)
    aulas = models.TextField(max_length=255)
    hora_funcionamento = models.DateTimeField()
    #gerente = models.ForeignKey()

class Maquina(models.Model):
    nome = models.TextField(max_length=255 ,primary_key=True)
    grupo_muscular = models.TextField(max_length=255)    
    marca = models.TextField(max_length=255)
    data_compra = models.DateField()
    ult_manutencao = models.DateField()
    fornecedor = models.TextField(max_length=255)
    prazo_manutencao = models.DateField()
    prox_manutencao = models.DateField()
    responsavel = models.TextField(max_length=225)
    #unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

