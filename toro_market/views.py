from django.shortcuts import render, get_object_or_404

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ProjectimageSerailizer

# class to check if the user type is a business 
class IsBusiness(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_business_user 


# Class to list all the energy projects available to be invested on 
class ProjectReadView(APIView):
    def get(sefl, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

# class to create a new energy project 
class ProjectCreateView(APIView):
   permission_classes = [permissions.IsAuthenticated, IsBusiness]

   def post(self, request):
       serializer = ProjectSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
# class to return details of one energy project
class ProjectDetailView(APIView):
    def get(self, request, pk):
        project = get_object_or_404(project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
#class to update a particular energy project 
class projectUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBusiness]

    def put(self, request, pk):
       project = get_object_or_404(Project, pk=pk)
       serializer = ProjectSerializer(project, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class to delete a particular energy project 
class ProjectDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBusiness] 

    def delete(self, request, pk):
       project = get_object_or_404(Project, pk=pk)
       project.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


