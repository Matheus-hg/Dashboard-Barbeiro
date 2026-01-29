from django.urls import path
from . import views

urlpatterns = [
    # Exemplo de rota: lista de agendamentos
    path('', views.lista_agendamentos, name='lista_agendamentos'),
]
