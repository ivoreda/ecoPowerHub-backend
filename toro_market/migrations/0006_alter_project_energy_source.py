# Generated by Django 4.2.7 on 2023-11-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toro_market', '0005_rename_images_projectimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='energy_source',
            field=models.CharField(choices=[('Solar', 'Solar'), ('Petroleum', 'Petroleum')], max_length=20),
        ),
    ]