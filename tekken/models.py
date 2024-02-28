from django.db import models

# Create your models here.

class Tekken(models.Model):
    nome = models.CharField(max_length = 100)
    nacionalidade = models.CharField(max_length = 100)
    estilo_de_luta = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome