# apps/agendamentos/models.py

from django.db import models
from apps.produtos.models import Produto

class Agendamento(models.Model):
    cliente = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE)
    servico = models.ForeignKey("servicos.Servico", on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente} - {self.servico} ({self.data_hora})"
    
    @property
    def receita_total(self):
        # preço do serviço
        total = float(self.servico.preco)
        # soma dos produtos vinculados
        for pa in self.produtos.all():
            total += float(pa.produto.preco) * pa.quantidade
        return total


class ProdutoAgendamento(models.Model):
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, related_name="produtos")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade} para {self.agendamento}"
