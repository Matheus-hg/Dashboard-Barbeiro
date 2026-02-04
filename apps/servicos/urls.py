from django.urls import path
from .views import lista_servicos, novo_servico, editar_servico, excluir_servico

app_name = "servicos"

urlpatterns = [
    path('', lista_servicos, name='lista_servicos'),
    path('novo/', novo_servico, name='novo_servico'),
    path('editar/<int:servico_id>/', editar_servico, name='editar_servico'),
    path('excluir/<int:servico_id>/', excluir_servico, name='excluir_servico'),
]
