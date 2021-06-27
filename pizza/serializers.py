from rest_framework import serializers
from .models import Pizza

'''
      The HyperlinkedModelSerializer class is similar to the 
      ModelSerializer class except that it uses hyperlinks to 
      represent relationships, rather than primary keys. By 
      default the serializer will include a url field instead 
      of a primary key field.

'''

class PizzaSerializer(serializers.ModelSerializer):
      
      class Meta:
            model = Pizza
            fields = '__all__'
