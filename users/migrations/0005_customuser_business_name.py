# Generated by Django 4.2.7 on 2023-11-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_share_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='business_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]