# Generated by Django 4.2.7 on 2023-11-10 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toro_market', '0004_remove_projectimage_project_content_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectimage',
            old_name='images',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image2',
        ),
    ]