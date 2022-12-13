from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('pizza', views.index_pizzas, name='index_pizzas'),
    path('pizza/<int:pizza_id>',views.show_pizza, name='show_pizza'),
    path('ingrediente', views.index_ingredientes,name='index_ingredientes'),
    path('ingrediente/<int:ingrediente_id>', views.show_ingrediente,name='show_ingrediente'),
    path('masa', views.index_masas,name='index_masas'),
    path('masa/<int:masa_id>', views.show_masa,name='show_masa'),

]
