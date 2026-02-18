from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import logout
from apps.clientes.models import Cliente
from apps.agendamentos.models import Agendamento
from apps.produtos.models import Produto
import json

def get_agendamentos_por_dia(data):
    """Retorna todos os agendamentos de um dia específico."""
    return Agendamento.objects.filter(data_hora__date=data)

def get_agendamentos_por_intervalo(inicio, fim):
    """Retorna todos os agendamentos dentro de um intervalo de datas."""
    return Agendamento.objects.filter(data_hora__date__range=(inicio, fim))

def index(request):
    hoje = timezone.localdate()
    data_str = request.GET.get("data")
    quick = request.GET.get("quick")

    dias, cortes = [], []

    # --- Seleção de período ---
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

        # preparar dados para o gráfico
        dia_atual = inicio_semana
        while dia_atual <= fim_semana:
            ag_dia = get_agendamentos_por_dia(dia_atual)
            dias.append(dia_atual.strftime("%d/%m"))
            cortes.append(ag_dia.count())
            dia_atual += timedelta(days=1)

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

    # --- Estatísticas ---
    cabelos_cortados = agendamentos.count()
    receita = sum([ag.receita_total for ag in agendamentos])  # agora usa serviço + produtos
    clientes = agendamentos.values("cliente").distinct().count()

    # --- Produtos ---
    produtos = Produto.objects.all()

    # --- Contexto ---
    contexto = {
        "agendamentos": agendamentos,
        "cabelos_cortados": cabelos_cortados,
        "receita": receita,
        "clientes": clientes,
        "data": data,
        "dias": json.dumps(dias),
        "cortes": json.dumps(cortes),
        "produtos": produtos,
    }

    return render(request, "index.html", contexto)


def custom_logout(request):
    logout(request)
    return redirect('dashboard:home')  # volta para a home


@login_required
def home(request):
    hoje = now().date()
    agendamentos = Agendamento.objects.filter(data_hora__date=hoje).order_by("data_hora")

    cabelos_cortados = agendamentos.count()
    receita = float(sum([ag.servico.preco for ag in agendamentos]))  # conversão para float
    clientes = agendamentos.values("cliente").distinct().count()

    context = {
        "agendamentos": agendamentos,
        "cabelos_cortados": cabelos_cortados,
        "receita": receita,
        "clientes": clientes,
        "data": hoje,
        "dias": "[]",
        "receitas": "[]",
        "cortes": "[]",
    }
    return render(request, "index.html", context)
