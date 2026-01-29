"""
URL configuration for dashboard_barbeiro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from apps.clientes.views import custom_logout

urlpatterns = [
    path('', include('dashboard.urls')), # página inicial
    path('clientes/', include('apps.clientes.urls')),  # rota para a home do app clientes
    path('servicos/', include('apps.servicos.urls')),
    path('agendamentos/', include('apps.agendamentos.urls')),
    path('logout/', custom_logout, name='logout'),
    path('admin/', admin.site.urls),          # rota para o painel admin
]
