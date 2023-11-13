from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from uuid import uuid4

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# Defining energy sources

ENERGY_SOURCES = (
    ("Solar", "Solar"),
    ('Petroleum' ,'Petroleum' )
)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20)
    project_description = models.TextField(blank=True, null=True)
    energy_capacity = models.CharField(max_length=20)
    energy_source = models.CharField(choices=ENERGY_SOURCES, max_length=20)
    location = models.CharField(max_length=50)
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.project_name


"""

Instead of creating two image variable 
Define a new class to handle images 
Assuming there is going to be a directory that stores the images 
However using a UUIDFIELD won't allow form some ORM
To be able to use them i utilised the GenericForeignKey 

"""


class ProjectImage(models.Model):
    # image model should go away
    project = models.ForeignKey(Project, 
                                on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="project_images/")


    def __str__(self) -> str:
        return self.project.project_name


