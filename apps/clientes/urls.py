from django.urls import path
from .views import lista_clientes, CustomLoginView

urlpatterns = [
    path('', lista_clientes, name='lista_clientes'),
    path('login/', CustomLoginView.as_view(), name='login'),
]