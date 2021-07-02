from django.shortcuts import render, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import PizzaSerializer
from . models import Pizza



@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/pizzas/',
        '/Fore Resume Site Data Please use following urls/',
        '/api/skills',
        '/api/projects',
        '/api/languages/',
        '/api/tools',
        
    ]
    
    return Response(routes)



@api_view(['GET'])
def getPizzas(request):
  
  pizzas = Pizza.objects.all()

  serailizer = PizzaSerializer(pizzas, many=True)
  
  return Response(serailizer.data)
  


