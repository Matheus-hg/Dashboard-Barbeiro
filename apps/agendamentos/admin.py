from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'data_hora')
    list_filter = ('data_hora', 'servico')
    search_fields = ('cliente__nome', 'servico__nome')
# Register your models here.