from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente   # conecta o formulário ao modelo Cliente
        fields = ['nome', 'email', 'telefone']  # campos que vão aparecer no formulário
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Digite o nome',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Digite o email',
                'class': 'form-control'
            }),
            'telefone': forms.TextInput(attrs={
                'placeholder': 'Digite o telefone',
                'class': 'form-control'
            }),
        }
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'telefone': 'Telefone',
        }
