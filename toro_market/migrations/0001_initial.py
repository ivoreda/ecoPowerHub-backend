# Generated by Django 4.2.7 on 2023-11-10 14:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=20)),
                ('project_description', models.TextField(blank=True, null=True)),
                ('energy_capacity', models.CharField(max_length=20)),
                ('energy_source', models.CharField(choices=[('tRR', 'transad'), ('sff', 'grests')], max_length=3)),
                ('location', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_object_id', models.UUIDField()),
                ('images', models.ImageField(upload_to='project_images/')),
                ('project_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
