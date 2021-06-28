from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.getRoutes, name="routes"),
    path('api/pizzas/', views.getPizzas, name="pizzas"),
     
]