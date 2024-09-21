from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import RegistroForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('paginas/index.htlm')
    else:
        form = RegistroForm()
    return render(request, 'paginas/register.html', {'form': form})

def login(request):
    return render(request, 'paginas/login.html')
 
def index(request):
    return render(request, 'paginas/index.html')

def about(request):
    return render(request, 'paginas/about.html')

def contact(request):
    return render(request, 'paginas/contact.html')
    
     