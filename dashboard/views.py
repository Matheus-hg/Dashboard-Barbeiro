from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from apps.clientes.models import Cliente
from apps.agendamentos.models import Agendamento
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
from datetime import datetime, timedelta
import json

def get_agendamentos_por_dia(data):
    """Retorna todos os agendamentos de um dia específico (com timezone)."""
    inicio = timezone.make_aware(datetime.combine(data, datetime.min.time()))
    fim = timezone.make_aware(datetime.combine(data, datetime.max.time()))
    return Agendamento.objects.filter(data_hora__range=(inicio, fim))

def get_agendamentos_por_intervalo(inicio, fim):
    """Retorna todos os agendamentos dentro de um intervalo de datas."""
    inicio = timezone.make_aware(datetime.combine(inicio, datetime.min.time()))
    fim = timezone.make_aware(datetime.combine(fim, datetime.max.time()))
    return Agendamento.objects.filter(data_hora__range=(inicio, fim))

def index(request):
    hoje = timezone.localdate()
    data_str = request.GET.get("data")
    quick = request.GET.get("quick")

    dias, receitas, cortes = [], [], []

    if quick == "hoje":
        data = hoje
        agendamentos = get_agendamentos_por_dia(data)

    elif quick == "amanha":
        data = hoje + timedelta(days=1)
        agendamentos = get_agendamentos_por_dia(data)

    elif quick == "ontem":
        data = hoje - timedelta(days=1)
        agendamentos = get_agendamentos_por_dia(data)

    elif quick == "semana":
        inicio_semana = hoje - timedelta(days=hoje.weekday())  # segunda-feira
        fim_semana = inicio_semana + timedelta(days=6)         # domingo
        agendamentos = get_agendamentos_por_intervalo(inicio_semana, fim_semana)
        data = f"{inicio_semana.strftime('%d/%m')} - {fim_semana.strftime('%d/%m')}"

    elif quick == "mes":
        inicio_mes = hoje.replace(day=1)
        if inicio_mes.month == 12:
            proximo_mes = inicio_mes.replace(year=inicio_mes.year+1, month=1, day=1)
        else:
            proximo_mes = inicio_mes.replace(month=inicio_mes.month+1, day=1)
        fim_mes = proximo_mes - timedelta(days=1)

        agendamentos = get_agendamentos_por_intervalo(inicio_mes, fim_mes)
        data = f"{inicio_mes.strftime('%d/%m')} - {fim_mes.strftime('%d/%m')}"

        # preparar dados para o gráfico
        dia_atual = inicio_mes
        while dia_atual <= fim_mes:
            ag_dia = get_agendamentos_por_dia(dia_atual)
            dias.append(dia_atual.strftime("%d/%m"))
            receitas.append(sum([ag.servico.preco for ag in ag_dia]))
            cortes.append(ag_dia.count())
            dia_atual += timedelta(days=1)

    elif data_str:
        try:
            data = datetime.strptime(data_str, "%Y-%m-%d").date()
        except ValueError:
            data = hoje
        agendamentos = get_agendamentos_por_dia(data)

    else:
        data = hoje
        agendamentos = get_agendamentos_por_dia(data)

    # --- ESTATÍSTICAS ---
    cabelos_cortados = agendamentos.count()
    receita = sum([ag.servico.preco for ag in agendamentos])
    clientes = agendamentos.values("cliente").distinct().count()

    return render(request, "index.html", {
        "agendamentos_do_dia": agendamentos,
        "cabelos_cortados": cabelos_cortados,
        "receita": receita,
        "clientes": clientes,
        "data": data,
        "dias": json.dumps(dias),
        "receitas": json.dumps(receitas),
        "cortes": json.dumps(cortes),
    })



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
