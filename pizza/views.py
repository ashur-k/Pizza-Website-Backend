from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import PizzaSerializer
from . models import Pizza


@api_view(['GET'])
def getPizzas(request):
  
  pizzas = Pizza.objects.all()

  serailizer = PizzaSerializer(pizzas, many=True)
  
  return Response(serailizer.data)
  


