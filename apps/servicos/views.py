from django.shortcuts import render
from .models import Servico

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/lista.html', {'servicos': servicos})

# Create your views here.
