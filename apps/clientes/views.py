from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import Cliente
from django.contrib import messages

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        # quando o login for válido, adiciona a mensagem
        messages.success(self.request, "Login realizado com sucesso!") 
        return super().form_valid(form)
        
def custom_logout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('/clientes/login/')
# Create your views here.
