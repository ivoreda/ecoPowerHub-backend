from django.shortcuts import render, get_object_or_404

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ProjectimageSerailizer, CreateProjectSerializer

# class to check if the user type is a business 
# there is an issue here
class IsBusiness(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type != "Business":
            return Response({"status": False, "message": "You do not have permission to access this resource."})
        # return request.user.user_type 


# Class to list all the energy projects available to be invested on 
class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

# create view for getting user specific energy projects
# projects = Project.objects.filter(user=request.user)


# class to create a new energy project 
class ProjectCreateView(APIView):
   permission_classes = [permissions.IsAuthenticated, IsBusiness]

   def post(self, request):
       serializer = CreateProjectSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(user=request.user)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
# class to return details of one energy project
class ProjectDetailView(APIView):
    def get(self, request, pk):
        project = get_object_or_404(project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
#class to update a particular energy project 
class ProjectUpdateView(APIView):
    # add permission to make sure that the user updating is the user that created the project
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
    # add permission to make sure that the user deleting is the user that created the project
    permission_classes = [permissions.IsAuthenticated, IsBusiness] 

    def delete(self, request, pk):
       project = get_object_or_404(Project, pk=pk)
       project.delete()
       return Response({"status": True, "message": "Project deleted successfully."}, status=status.HTTP_200_OK)


