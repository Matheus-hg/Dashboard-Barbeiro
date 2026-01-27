from django.db import models

from django.db import models
from apps.clientes.models import Cliente
from apps.servicos.models import Servico

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"


# Create your models here.
