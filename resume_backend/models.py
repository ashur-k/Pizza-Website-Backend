from django.db import models
from django.contrib.postgres.fields import ArrayField


class Skills(models.Model):    
      class Meta:     
            verbose_name_plural = 'Skills'        
      
      Icon = models.CharField(max_length=300)
      title = models.CharField(max_length=200)
      about = models.CharField(max_length=300)
      
      def __str__(self):
            return self.title


class Project(models.Model):    
      class Meta:     
            verbose_name_plural = 'Projects'

      name = models.CharField(max_length=200)
      image_path = models.CharField(max_length=500)
      description = models.TextField()
      category = ArrayField(
            models.CharField(max_length=200)
            )
      key_techs = ArrayField(
            models.CharField(max_length=200)
            )
      deployed_url = models.CharField(max_length=500)
      github_url = models.CharField(max_length=500)
      
      def __str__(self):
            return self.name


class Language(models.Model):  
      
      class Meta:     
            verbose_name_plural = 'Languages'
      
      name = models.CharField(max_length=200)
      level = models.CharField(max_length=200)
      
      def __str__(self):
            return self.name
      

class Tool(models.Model):
      
      class Meta:     
            verbose_name_plural = 'Tools'
      
      name = models.CharField(max_length=200)
      level = models.CharField(max_length=200)
      
      def __str__(self):
            return self.name 