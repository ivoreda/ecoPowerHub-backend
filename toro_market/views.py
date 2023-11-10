from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

# Create your views here.
def is_business_user(user):
    return user.type == 'business'

# Class to listg all the energy projects available to be invested on 
class Homeview(ListView):
    model = Project 

@method_decorator(user_passes_test(is_business_user), name='dispatch')
class ProjectCreateView(CreateView):
    model = Project
    fields = ['project_name', 'project_description', 'energy_capacity', 'energy_source', 'location', 'price']
    template_name = ''


class ProjectDetailView(DetailView):
    model = Project 
    template_name = ''

@method_decorator(user_passes_test(is_business_user), name='dispatch')
class ProjectUpdateView(UpdateView):
    model = Project 
    fields = ['project_name', 'project_description', 'energy_capacity', 'energy_source', 'location', 'price']
    template_name = ''

@method_decorator(user_passes_test(is_business_user), name='dispatch')
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = ''
    success_url = '/projects/'