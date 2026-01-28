from django.urls import path 
from . import views
from .views import home, CustomLoginView

urlpatterns = [ 
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login')
]