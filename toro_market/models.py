from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from uuid import uuid4

# Create your models here.
# create a model for energy product
# one to one relationship to product from user/business
"""
id
project name
project description
energy capacity
energy source
location
price
image1 
image2

created_at
updated_at
"""


"""
only businesses can create energy product listing



"""


# Defining energy sources 

ENERGY_SOURCES = (
    ()
)

class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_name = models.CharField(max_length=20)
    project_description = models.TextField(blank=True, null=True)
    energy_capacity = models.CharField(max_length=20)
    energy_source = models.CharField(choices=ENERGY_SOURCES, max_length=3)
    location = models.CharField(max_length=50)
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


"""

Instead of creating two image variable 
Define a new class to handle images 
Assuming there is going to be a directory that stores the images 
However using a UUIDFIELD won't allow form some ORM
To be able to use them i utilised the GenericForeignKey 

"""

class ProjectsImages(models.Model):
    project_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    project_object_id = models.UUIDField()
    project = GenericForeignKey('project_content_type', 'project_object_id')
    images = models.ImageField(upload_to='project_images/')

