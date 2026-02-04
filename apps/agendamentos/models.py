from django.db import models
from apps.clientes.models import Cliente
from apps.servicos.models import Servico  # supondo que você tenha um app de serviços

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()  # <-- provavelmente o nome correto é data_hora

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico.nome} em {self.data_hora}"
