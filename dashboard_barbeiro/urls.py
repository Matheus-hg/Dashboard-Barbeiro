"""
URL configuration for dashboard_barbeiro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from apps.clientes.views import custom_logout

urlpatterns = [
    path('', include('dashboard.urls')),  # página inicial -> index.html
    path('clientes/', include('apps.clientes.urls')),  # rotas do app clientes
    path('servicos/', include('apps.servicos.urls')),  # rotas do app serviços
    path('agendamentos/', include('apps.agendamentos.urls')),  # rotas do app agendamentos
    path('logout/', custom_logout, name='logout'),  # logout centralizado
    path('admin/', admin.site.urls),
]
