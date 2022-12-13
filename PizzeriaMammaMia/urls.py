from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('pizza', views.PizzaListView.as_view(), name='index_pizzas'),
    path('pizza/<int:pk>',views.PizzaDetailView.as_view(), name='show_pizza'),
    path('ingrediente', views.index_ingredientes,name='index_ingredientes'),
    path('ingrediente/<int:ingrediente_id>', views.show_ingrediente,name='show_ingrediente'),
    path('masa', views.index_masas,name='index_masas'),
    path('masa/<int:pk>', views.MasaDetailView.as_view(),name='show_masa'),

]
