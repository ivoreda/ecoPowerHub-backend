from django.contrib import admin
from .models import Project, Transaction, Investment

# Register your models here.
admin.site.register(Project)
admin.site.register(Transaction)
admin.site.register(Investment)
