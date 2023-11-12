"""
URL configuration for ecoPowerHub_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from toro_market.views import ProjectCreateView, ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', ProjectListView.as_view(), name='home'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<uuid:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/update/<uuid:pk>/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/delete/<uuid:pk>/', ProjectDeleteView.as_view(), name='project-delete'),
        
]
