from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento
from .forms import AgendamentoForm

# Lista todos os agendamentos
@login_required
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.select_related("cliente", "servico").all()
    return render(request, "agendamentos/lista.html", {"agendamentos": agendamentos})

# Cria um novo agendamento
@login_required
def novo_agendamento(request):
    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agendamentos:lista_agendamentos")
    else:
        form = AgendamentoForm()
    return render(request, "agendamentos/novo.html", {"form": form})

# Edita um agendamento existente
@login_required
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == "POST":
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect("agendamentos:lista_agendamentos")
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, "agendamentos/editar.html", {"form": form})

# Exclui um agendamento
@login_required
def excluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == "POST":
        agendamento.delete()
        return redirect("agendamentos:lista_agendamentos")
    return render(request, "agendamentos/confirmar_exclusao.html", {"agendamento": agendamento})
