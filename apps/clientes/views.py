from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm

def lista_clientes(request):
    # Busca todos os clientes
    clientes = Cliente.objects.all()

    # Se for um POST, significa que o formulário foi enviado
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('lista_clientes')  # redireciona para a lista
    else:
        form = ClienteForm()

    # Renderiza lista.html com clientes e formulário
    return render(request, 'clientes/lista.html', {
        'clientes': clientes,
        'form': form,
    })


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, f"Cliente {cliente.nome} atualizado com sucesso!")
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)

    # Sempre retorna um HttpResponse
    return render(request, 'clientes/editar.html', {
        'form': form,
        'cliente': cliente
    })


def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, f"Cliente {cliente.nome} excluído com sucesso!")
        return redirect('lista_clientes')

    # Página de confirmação
    return render(request, 'clientes/confirmar_exclusao.html', {
        'cliente': cliente
    })


class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        # quando o login for válido, adiciona a mensagem
        messages.success(self.request, "Login realizado com sucesso!") 
        return super().form_valid(form)


def custom_logout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')  # usa o nome da rota de login
