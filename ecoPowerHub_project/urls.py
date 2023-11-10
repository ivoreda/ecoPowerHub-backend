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
from toro_market.views import ProjectCreateView, ProjectDeleteView, ProjectDetailView, ProjectUpdateView, Homeview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', Homeview.as_view(), name='home'), 
    path('projects/new/', ProjectCreateView.as_view(), name='project_new'),
    path('projects/<uuid:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<uuid:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/<uuid:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    
]
