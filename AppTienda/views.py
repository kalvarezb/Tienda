from django.http import HttpResponse
import requests
from django.shortcuts import render
from django.shortcuts import redirect
from  . import models
from .forms import VentaForm,LoginForm

def index(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    return render(request,'index.html',{'dolar': data['dolar']['valor']})


def login(request):
    return render(request,'login.html')

def registroVenta(request):
    form = VentaForm()
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.save()
            return redirect('index')
    else:
        form = VentaForm()
    return render(request, 'registroVenta.html', {'form': form})