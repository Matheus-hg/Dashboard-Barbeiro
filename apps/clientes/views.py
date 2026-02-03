from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'clientes/login.html'
    redirect_authenticated_user = True
    
def custom_logout(request):
    logout(request)
    return redirect('dashboard:home')  # redireciona para a home após logout


@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista.html", {"clientes": clientes})

@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    # lógica de edição...
    return render(request, "clientes/editar.html", {"cliente": cliente})

@login_required
def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        cliente.delete()
        return redirect("lista_clientes")
    return render(request, "clientes/confirmar_exclusao.html", {"cliente": cliente})
