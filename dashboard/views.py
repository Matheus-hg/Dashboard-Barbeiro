from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from apps.clientes.models import Cliente
from apps.agendamentos.models import Agendamento
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('dashboard:home')  # volta para a home


@login_required
def home(request):
    hoje = now().date()

    clientes_hoje = Cliente.objects.filter(data_cadastro__date=hoje).count()
    servicos_realizados = Agendamento.objects.filter(data_hora__date=hoje).count()
    receita_hoje = sum(
        ag.servico.preco for ag in Agendamento.objects.filter(data_hora__date=hoje)
    )
    agendamentos = Agendamento.objects.filter(data_hora__date=hoje).order_by("data_hora")

    context = {
        "clientes_hoje": clientes_hoje,
        "servicos_realizados": servicos_realizados,
        "receita_hoje": receita_hoje,
        "agendamentos": agendamentos,
    }
    return render(request, "index.html", context)
