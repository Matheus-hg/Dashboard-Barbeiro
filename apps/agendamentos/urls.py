from django.urls import path
from .views import lista_agendamentos, novo_agendamento, editar_agendamento, excluir_agendamento

app_name = "agendamentos"

urlpatterns = [
    path('', lista_agendamentos, name='lista_agendamentos'),
    path('novo/', novo_agendamento, name='novo_agendamento'),
    path('editar/<int:agendamento_id>/', editar_agendamento, name='editar_agendamento'),
    path('excluir/<int:agendamento_id>/', excluir_agendamento, name='excluir_agendamento'),
]
