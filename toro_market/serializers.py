from rest_framework import serializers
from .models import Project, ProjectImage


class ProjectSerializer(serializers.ModelSerializer):
    class meta:
        model = Project
        fields = ['id', 'project_name', 'project_description', 'energy_capacity', 'energy_source', 'location']


class ProjectimageSerailizer(serializers.ModelSerializer):
    class meta:
        model = ProjectImage
        fields = ['project', 'image']