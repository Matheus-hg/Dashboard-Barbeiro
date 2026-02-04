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
def lista_clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes:lista_clientes")
    else:
        form = ClienteForm()  # <-- garante que no GET o form existe

    clientes = Cliente.objects.all()
    return render(request, "clientes/lista.html", {
        "form": form,
        "clientes": clientes
    })


@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == "POST":
        cliente.nome = request.POST.get("nome")
        cliente.email = request.POST.get("email")
        cliente.telefone = request.POST.get("telefone")
        cliente.save()
        return redirect("clientes:lista_clientes")

    return render(request, "clientes/editar.html", {"cliente": cliente})


@login_required
def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == "POST":
        cliente.delete()
        return redirect("clientes:lista_clientes")

    return render(request, "clientes/confirmar_exclusao.html", {"cliente": cliente})
