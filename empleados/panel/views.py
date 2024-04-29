from django.shortcuts import render, redirect, HttpResponse
from .conexion import conexion
from .models import Clientes
# Create your views here.


def panel(request):
    if request.method == 'POST':
            return redirect('panel')
    else:
        clientes = Clientes.objects.all()
        return render(request, 'panel.html', {
            'clientes': clientes,
        })
        
        
        
def eliminar(request, id):
    return redirect('panel')


def editar(request, id):
    if request.method == 'POST':
            return redirect('panel')
    else:
        return render(request, 'editar.html')