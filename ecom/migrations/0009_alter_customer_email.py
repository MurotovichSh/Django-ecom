# Generated by Django 4.2 on 2023-04-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_rename_orders_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
