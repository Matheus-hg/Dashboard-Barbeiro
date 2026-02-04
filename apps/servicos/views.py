from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Servico
from .forms import ServicoForm

@login_required
def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, "servicos/lista.html", {"servicos": servicos})

@login_required
def novo_servico(request):
    if request.method == "POST":
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicos:lista_servicos")
    else:
        form = ServicoForm()
    return render(request, "servicos/novo.html", {"form": form})

@login_required
def editar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    if request.method == "POST":
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect("servicos:lista_servicos")
    else:
        form = ServicoForm(instance=servico)
    return render(request, "servicos/editar.html", {"form": form})

@login_required
def excluir_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    if request.method == "POST":
        servico.delete()
        return redirect("servicos:lista_servicos")
    return render(request, "servicos/confirmar_exclusao.html", {"servico": servico})
