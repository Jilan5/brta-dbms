# Generated by Django 4.2.4 on 2023-08-17 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_region_user_addr_user_blood_group_user_date_of_birth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_fixed_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=9, null=True)),
                ('engine_no', models.CharField(max_length=20, null=True, unique=True)),
                ('seat', models.IntegerField(null=True)),
                ('fuel_type', models.CharField(max_length=20, null=True)),
                ('engine_cc', models.IntegerField()),
                ('vehicle_class', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_variable_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fitness_st_date', models.DateField(blank=True, null=True)),
                ('fitness_exp_date', models.DateField(blank=True, null=True)),
                ('taxtoken_up_to', models.DateField(blank=True, null=True)),
                ('insurance_st_date', models.DateField(blank=True, null=True)),
                ('insurance_exp_date', models.DateField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('reg_st_date', models.DateField(blank=True, null=True)),
                ('reg_exp_date', models.DateField(blank=True, null=True)),
                ('request_with_payment', models.CharField(blank=True, max_length=200, null=True)),
                ('reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.vehicle_fixed_detail')),
            ],
        ),
    ]
