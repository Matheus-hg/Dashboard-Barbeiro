from django.urls import path
from . import views

urlpatterns = [
    path("", views.produtos, name="produtos"),
    path("editar/<int:pk>/", views.editar_produto, name="editar_produto"),
    path("excluir/<int:pk>/", views.excluir_produto, name="excluir_produto"),
]
