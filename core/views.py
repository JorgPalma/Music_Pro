from urllib.request import Request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForms
from django.contrib import messages

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'core/index.html', data)


def add_product(request):

    data = {
        'form': ProductoForms()
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'core/vendedor/agregar.html', data)

def list_product(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }


    return render(request, 'core/vendedor/listar.html', data)

def edit_product(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForms(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="list_product")
        data["form"] = formulario
            

    return render(request, 'core/vendedor/editar.html', data)

def delete_product(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="list_product")

def detail_product(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'productos': producto
    }

    return render(request,'core/detalle.html', data)