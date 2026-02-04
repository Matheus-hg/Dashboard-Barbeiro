from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    lista_clientes,
    editar_cliente,
    excluir_cliente,
    custom_logout,
)

app_name = "clientes"

urlpatterns = [
    path('', lista_clientes, name='lista_clientes'),
    path('editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('excluir/<int:cliente_id>/', excluir_cliente, name='excluir_cliente'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
]
