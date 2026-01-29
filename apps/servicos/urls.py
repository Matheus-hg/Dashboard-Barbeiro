from django.urls import path
from . import views

urlpatterns = [
    # Exemplo de rota: lista de serviços
    path('', views.lista_servicos, name='lista_servicos'),
]
