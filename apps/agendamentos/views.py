from django.shortcuts import render
from .models import Agendamento

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('data_hora')
    return render(request, 'agendamentos/lista.html', {'agendamentos': agendamentos})
# Create your views here.
