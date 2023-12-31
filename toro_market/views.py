from django.shortcuts import render, get_object_or_404

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project, Transaction, Investment
from .serializers import ProjectSerializer, CreateProjectSerializer, InvestSerializer, BuyProjectSerialier

from django.contrib.auth import get_user_model

User = get_user_model()

# class to check if the user type is a business
# there is an issue here


class IsBusiness(permissions.BasePermission):
    message = "You do not have permission to access this resource"

    def has_permission(self, request, view):
        return request.user.user_type == "Business"


class IsProjectOwner(permissions.BasePermission):
    message = "Ah shoot!, You can not edit this project"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

# Class to list all the energy projects available to be invested on


class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


# create view for getting user specific energy projects
# projects = Project.objects.filter(user=request.user)


class UserSpecificProjectView(APIView):
    permissions_classes = [permissions.IsAuthenticated, IsBusiness]

    def get(self, request):
        projects = Project.objects.filter(user=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


# class to create a new energy project
class ProjectCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBusiness]

    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"status": True, "message": "Project created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class to return details of one energy project


class ProjectDetailView(APIView):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


# class to update a particular energy project
class ProjectUpdateView(APIView):
    # add permission to make sure that the user updating is the user that created the project
    permission_classes = [permissions.IsAuthenticated, IsBusiness, IsProjectOwner]

    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Project updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class to delete a particular energy project


class ProjectDeleteView(APIView, IsProjectOwner):
    # add permission to make sure that the user deleting is the user that created the project
    permission_classes = [
        permissions.IsAuthenticated, IsBusiness, IsProjectOwner]

    def delete(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response(
            {"status": True, "message": "Project deleted successfully."},
            status=status.HTTP_200_OK,
        )


class BuyProjectView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BuyProjectSerialier

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        project = get_object_or_404(Project, pk=pk)
        if project:
            if serializer.is_valid():
                amount = serializer.data.get("amount")
                transaction = Transaction.objects.create(project=project, amount=amount, status="Done",
                                                        transaction_type="Project Payment")
                return Response({"status": True, "message": "Project Purchased successfully"}, status=status.HTTP_200_OK)
        return Response({"status": False, "message": "Project not found"}, status=status.HTTP_400_BAD_REQUEST)


class InvestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InvestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            business = serializer.data.get("business")
            percentage_of_business = serializer.data.get("percentage_of_business")
            amount_invested = serializer.data.get("amount_invested")

            user = User.objects.get(id=request.user.id)
            business_user = User.objects.get(id=business)

            investment = Investment.objects.create(user=user,
                                                business=business_user, 
                                                percentage_of_business=percentage_of_business, 
                                                amount_invested=amount_invested)

            

            transaction = Transaction.objects.create(business=business_user, status="Done",
                                                    transaction_type="Investment", amount=amount_invested)
            return Response({"status": True, "message": "Investment logged successfully"})
