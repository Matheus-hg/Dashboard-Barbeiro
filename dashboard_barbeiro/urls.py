"""
URL configuration for dashboard_barbeiro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # rota para o painel admin
    path('', include('apps.clientes.urls')),  # rota para a home do app clientes
]
