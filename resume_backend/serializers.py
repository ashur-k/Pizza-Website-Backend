from rest_framework import serializers

from . models import Skills, Project, Language, Tool

#, Category, keyTech

class SkillsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Skills
    fields = '__all__'
    


class ProjectSerializer(serializers.ModelSerializer):

  class Meta:
        model = Project
        fields = '__all__'
        

class LanguageSerializer(serializers.ModelSerializer):
  
  class Meta:
        model = Language
        fields = '__all__'


class ToolSerializer(serializers.ModelSerializer):
  
  class Meta:
        model = Tool
        fields = '__all__'