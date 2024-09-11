from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def index(request):
    return render(request, 'paginas/index.html')

def about(request):
    return render(request, 'paginas/about.html')

def contact(request):
    return render(request, 'paginas/contact.html')
    
     