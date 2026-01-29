from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from apps.clientes.models import Cliente
from apps.servicos.models import Servico
from apps.agendamentos.models import Agendamento

@login_required
def home(request):
    hoje = now().date()

    clientes_hoje = Cliente.objects.filter(data_cadastro__date=hoje).count()
    servicos_realizados = Agendamento.objects.filter(data_hora__date=hoje).count()
    receita_hoje = sum(
        ag.servico.preco for ag in Agendamento.objects.filter(data_hora__date=hoje)
    )
    agendamentos = Agendamento.objects.filter(data_hora__date=hoje).order_by("data_hora")
    servicos = Servico.objects.all()

    context = {
        "clientes_hoje": clientes_hoje,
        "servicos_realizados": servicos_realizados,
        "receita_hoje": receita_hoje,
        "agendamentos": agendamentos,
        "servicos": servicos,
    }
    return render(request, "index.html", context)

# Create your views here.
