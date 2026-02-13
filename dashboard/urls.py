from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="home"),   # <-- usa index como rota principal
    path("logout/", views.custom_logout, name="logout"),
]
