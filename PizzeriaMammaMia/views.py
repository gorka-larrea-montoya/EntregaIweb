from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *

# Create your views here.

def landing(request):
    pizzas = get_object_or_404(Pizza,pk=1)
    context = {'pizzas' : pizzas}
    return render(request,'landing.html',context)
    #TODO hacer que devuelva la pizza mas barata por cada tipo de masa
    #Esta magia de Bases de datos no se hacerla
    
def show_pizza(request,pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    masa = pizza.masa
    ingredientes = pizza.ingredientes.all()
    context = {'pizza' : pizza , 'masa': masa, 'ingredientes' : ingredientes}
    return render(request,'pizza.html',context)

def index_pizzas(request):
    pizzas = get_list_or_404(Pizza.objects.order_by('nombre'))
    context = {'lista_pizzas' : pizzas}
    return render(request, 'pizzas.html', context)

def show_masa(request,masa_id):
    masa = get_object_or_404(Masa,pk=masa_id)
    context = {'masa' : masa}
    return render(request, 'masa.html', context)

def index_masas(request):
    masas = get_list_or_404(Masa.objects.order_by('nombre'))
    context = {'masas' : masas}
    return render(request, 'masas.html', context)

def show_ingrediente(request,ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente,pk=ingrediente_id)
    context = {'ingrediente' : ingrediente}
    return render(request, 'ingrediente.html', context)

def index_ingredientes(request):
    ingredientes = get_list_or_404(Ingrediente.objects.order_by('nombre'))
    context = {'ingredientes' : ingredientes}
    return render(request, 'ingredientes.html', context)

