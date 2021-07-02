from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Skills, Project, Language, Tool
from .serializers import SkillsSerializer, ProjectSerializer, LanguageSerializer, ToolSerializer


@api_view(['GET'])
def getSkills(request):
  
  skills = Skills.objects.all()    
  serializer = SkillsSerializer(skills, many=True)
  
  return Response(serializer.data)


@api_view(['GET'])
def getProjects(request):
  
  projects = Project.objects.all()    
  serializer = ProjectSerializer(projects, many=True)
  
  return Response(serializer.data)


@api_view(['GET'])
def getLanguages(request):
  
  languages = Language.objects.all()    
  serializer = LanguageSerializer(languages, many=True)
  
  return Response(serializer.data)


@api_view(['GET'])
def getTools(request):
  
  tools = Tool.objects.all()    
  serializer = ToolSerializer(tools, many=True)
  
  return Response(serializer.data)