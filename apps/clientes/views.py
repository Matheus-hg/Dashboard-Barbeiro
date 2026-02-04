from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .models import Cliente
from .forms import ClienteForm

class CustomLoginView(LoginView):
    template_name = 'clientes/login.html'
    redirect_authenticated_user = True

def custom_logout(request):
    logout(request)
    return redirect('dashboard:home')

@login_required
def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:lista_clientes')
        else:
            form = ClienteForm()
        return render(request, 'clientes/novo.html', {'form': form})

@login_required
def lista_clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:lista_clientes")
    else:
        form = ClienteForm()  

    clientes = Cliente.objects.all()
    return render(request, "clientes/lista.html", {
        "form": form,
        "clientes": clientes
    })

@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)  # busca o cliente pelo ID
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)  # ESSENCIAL: instance=cliente
        if form.is_valid():
            form.save()
            return redirect("clientes:lista_clientes")
    else:
        form = ClienteForm(instance=cliente)  # formulário já preenchido

    return render(request, "clientes/editar.html", {"form": form})



@login_required
def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == "POST":
        cliente.delete()
        return redirect("clientes:lista_clientes")

    return render(request, "clientes/confirmar_exclusao.html", {"cliente": cliente})
