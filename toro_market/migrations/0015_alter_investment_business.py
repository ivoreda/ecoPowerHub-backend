# Generated by Django 4.2.7 on 2023-11-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toro_market', '0014_transaction_amount_alter_investment_amount_invested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='business',
            field=models.CharField(max_length=255),
        ),
    ]