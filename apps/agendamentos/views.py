from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento, ProdutoAgendamento
from .forms import AgendamentoForm, ProdutoAgendamentoForm

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
        produto_form = ProdutoAgendamentoForm(request.POST)
        if form.is_valid() and produto_form.is_valid():
            agendamento = form.save()
            produto_agendamento = produto_form.save(commit=False)
            produto_agendamento.agendamento = agendamento
            produto_agendamento.save()
            return redirect("agendamentos:lista_agendamentos")
    else:
        form = AgendamentoForm()
        produto_form = ProdutoAgendamentoForm()

    return render(request, "agendamentos/novo.html", {
        "form": form,
        "produto_form": produto_form,
    })


# Adiciona um novo produto
def adicionar_produto(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    if request.method == "POST":
        form = ProdutoAgendamentoForm(request.POST)
        if form.is_valid():
            produto_agendamento = form.save(commit=False)
            produto_agendamento.agendamento = agendamento
            produto_agendamento.save()
            return redirect("agendamentos:detalhe_agendamento", agendamento_id=agendamento.id)
    else:
        form = ProdutoAgendamentoForm()

    return render(request, "agendamentos/adicionar_produto.html", {"form": form, "agendamento": agendamento})

# Edita um agendamento existente
@login_required
def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    if request.method == "POST":
        form = AgendamentoForm(request.POST, instance=agendamento)
        produto_form = ProdutoAgendamentoForm(request.POST)
        if form.is_valid() and produto_form.is_valid():
            form.save()
            produto_agendamento = produto_form.save(commit=False)
            produto_agendamento.agendamento = agendamento
            produto_agendamento.save()
            return redirect("agendamentos:lista_agendamentos")
    else:
        form = AgendamentoForm(instance=agendamento)
        produto_form = ProdutoAgendamentoForm()

    return render(request, "agendamentos/editar.html", {
        "form": form,
        "produto_form": produto_form,
        "agendamento": agendamento,
    })



# Exclui um agendamento
@login_required
def excluir_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == "POST":
        agendamento.delete()
        return redirect("agendamentos:lista_agendamentos")
    return render(request, "agendamentos/confirmar_exclusao.html", {"agendamento": agendamento})
