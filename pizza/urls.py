from django.urls import path
from . import views

urlpatterns = [
    path('pizzas/', views.getPizzas, name="pizzas"),
     
]