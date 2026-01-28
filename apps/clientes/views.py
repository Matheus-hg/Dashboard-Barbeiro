from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'index.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

# Create your views here.
