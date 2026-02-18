from django import forms
from .models import Agendamento
from .models import ProdutoAgendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'servico', 'data_hora']  # use o nome correto do campo
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ProdutoAgendamentoForm(forms.ModelForm):
    class Meta:
        model = ProdutoAgendamento
        fields = ["produto", "quantidade"]
