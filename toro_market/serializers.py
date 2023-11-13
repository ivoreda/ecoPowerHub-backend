from rest_framework import serializers
from .models import Project, ProjectImage


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



class ProjectimageSerailizer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['project', 'image']