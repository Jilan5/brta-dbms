# Generated by Django 4.2.4 on 2023-08-17 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vehicle_fixed_detail_vehicle_variable_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='region_id',
        ),
    ]
