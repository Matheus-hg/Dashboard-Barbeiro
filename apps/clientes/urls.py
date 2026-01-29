from django.urls import path 
from .views import lista_clientes, CustomLoginView, custom_logout

urlpatterns = [ 
    path('', lista_clientes, name='lista_clientes'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
]