from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *

# Create your views here.

def landing(request):
    return HttpResponse("HolaMundo Landing")
    
def show_pizza(request,pizza_id):
    #TODO
    return HttpResponse("HolaMundo show_pizza")

def index_pizzas(request):
    #TODO
    return HttpResponse("HolaMundo index_pizzas")

def show_masa(request,masa_id):
    #TODO
    return HttpResponse("HolaMundo show_masa")

def index_masa(request):
    #TODO
    return HttpResponse("HolaMundo index_masa")

def show_ingrediente(request,ingrediente_id):
    #TODO
    return HttpResponse("HolaMundo show_ingrediente")

def index_ingredientes(request):
    #TODO
    return HttpResponse("HolaMundo index_ingrediente")     

