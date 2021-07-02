from django.contrib import admin
from . models import Skills, Project, Language, Tool

  

class ProjectAdmin(admin.ModelAdmin):
  
    list_display = ['id', 'name']



admin.site.register(Skills)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(Tool)
