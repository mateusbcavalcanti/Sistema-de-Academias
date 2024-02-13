from django.db import models

class Treino(models.Model):
    id_treino = models.AutoField(primary_key=True)
    aluno = models.TextField(max_length=255)
    treino = models.TextField(max_length=255)