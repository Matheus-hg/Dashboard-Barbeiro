from django.db import models

from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    duracao_minutos = models.IntegerField()

    def __str__(self):
        return self.nome


# Create your models here.
