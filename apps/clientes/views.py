from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Dashboard Barbeiro está rodando')
# Create your views here.
