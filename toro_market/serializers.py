from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'user', 'project_name', 'project_description', 
                'energy_capacity', 'energy_source', 'location', 'price']

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_name', 'project_description', 'energy_capacity', 
                    'energy_source', 'location', 'price']
