from rest_framework import serializers
from .models import Project, Transaction, Investment


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


class BuyProjectSerialier(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount']


class InvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ["business",
                  "percentage_of_business",
                  "amount_invested",]
