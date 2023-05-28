from django.db import models


class Atividade(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo
