from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import DetailView, ListView
from .models import *

# Create your views here.

def landing(request):
    pizzas = []
    
    tiposdemasa = get_list_or_404(Masa.objects.order_by('id'))
    for i in tiposdemasa:
        pizzs = get_list_or_404(Pizza.objects.order_by('precio'),masa=i)
        pizzas.append(pizzs[0])

    context = {'pizzas' : pizzas}
    return render(request,'landing.html',context)
    
class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'pizza.html'
    def get_context_data(self, **kwargs):
        context = super(PizzaDetailView,self).get_context_data(**kwargs)
        return context

#def show_pizza(request,pizza_id):
#    pizza = get_object_or_404(Pizza, pk=pizza_id)
#    masa = pizza.masa
#    ingredientes = pizza.ingredientes.all()
#    context = {'pizza' : pizza , 'masa': masa, 'ingredientes' : ingredientes}
#    return render(request,'pizza.html',context)

class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzas.html'
    queryset = Pizza.objects.order_by('id')

#def index_pizzas(request):
 #   pizzas = get_list_or_404(Pizza.objects.order_by('nombre'))
  #  context = {'lista_pizzas' : pizzas}
   # return render(request, 'pizzas.html', context)

#class MasaDetailView(DetailView):
#    model = Masa
#    template_name = 'masa.html'
#    
#    def get_context_data(self, **kwargs):
#        context = super(MasaDetailView,self).get_context_data(**kwargs)
#        #TODO pizzas = get_list_or_404(Pizza,masa)
#        return context

def show_masa(request,masa_id):
    masa = get_object_or_404(Masa,pk=masa_id)
    pizzas = get_list_or_404(Pizza,masa=masa_id)
    context = {'masa' : masa, 'pizzas' : pizzas}
    return render(request, 'masa.html', context)

class MasaListView(ListView):
    model : Masa
    template_name = "masas.html"
    queryset = Masa.objects.order_by('id')

#def index_masas(request):
#    masas = get_list_or_404(Masa.objects.order_by('nombre'))
#    context = {'masas' : masas}
#    return render(request, 'masas.html', context)



def show_ingrediente(request,ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente,pk=ingrediente_id)
    pizzas = get_list_or_404(Pizza,ingredientes=ingrediente_id)
    context = {'ingrediente' : ingrediente, 'pizzas' : pizzas}
    return render(request, 'ingrediente.html', context)
        
class IngredienteListView(ListView):
    model : Ingrediente
    template_name = "ingredientes.html"
    queryset = Ingrediente.objects.order_by('id')     

#def index_ingredientes(request):
#    ingredientes = get_list_or_404(Ingrediente.objects.order_by('nombre'))
#    context = {'ingredientes' : ingredientes}
#       return render(request, 'ingredientes.html', context)

