from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    dclass = (
        ('Learner License','Learner License'),
        ('Professional License','Professional License'),
        ('Heavy Vehicle','Heavy Vehicle'),
        ('Lite Vehicle','Lite Vehicle'),
        ('Instructor License','Instructor License')
    )
    name= models.CharField(max_length=200, null= True)
    user_id = models.CharField(unique=True, max_length=11, null=True )
    license_no= models.CharField(unique= True, max_length=9, null=True)
    addr = models.CharField(max_length=200, null=True)
    nid = models.CharField(unique=True, max_length=13, null=True)
    date_of_birth= models.DateField(null=True)
    blood_group = models.CharField(max_length=4,null=True)
    driver_class = models.CharField(max_length=20, default='DEFAULT VALUE',null=False, choices=dclass)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, null=True, blank=True)
    

    USERNAME_FIELD= 'user_id'
    REQUIRED_FIELDS= []

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=50, null=True)
    suffix = models.CharField(max_length=20, null=True)
    serial = models.CharField(unique=True, max_length=3, null=True)

    def __str__(self):
        return self.name


class Vehicle_fixed_detail(models.Model):
    vehicle_type= (
        ('SUV', 'SUV'),
        ('SEDAN', 'SEDAN'),
        ('BIKE', 'BIKE'),
        ('3-WHEELER','3-WHEELER'),
        ('TRUCK','TRUCK'),
        ('BUS','BUS')
        )
    fuel_type= (
        ('GAS','GAS'),
        ('PATROL','PATROL'),
        ('DIESEL','DIESEL'),
        ('OCTANE', 'OCTANE'),
    )
    client_id= models.CharField( max_length=9, null=True)
    engine_no= models.CharField(unique=True, max_length=20, null=True)
    seat=models.IntegerField(null=True)
    fuel_type=models.CharField(max_length=20, null=True, choices=fuel_type)
    engine_cc=models.IntegerField()
    vehicle_class= models.CharField(max_length=20,null=True, choices=vehicle_type)

    def __str__(self):
        return str(self.id)

class Vehicle_variable_details(models.Model):
    reg_no = models.OneToOneField(Vehicle_fixed_detail, on_delete=models.CASCADE)
    fitness_st_date=models.DateField(null=True,blank=True)
    fitness_exp_date=models.DateField(null=True,blank=True)
    taxtoken_up_to =models.DateField(null=True,blank=True)
    insurance_st_date=models.DateField(null=True,blank=True)
    insurance_exp_date=models.DateField(null=True,blank=True)
    color= models.CharField(max_length=10, null=True,blank=True)
    reg_st_date= models.DateField(null=True,blank=True)
    reg_exp_date= models.DateField(null=True,blank=True)
    request_with_payment= models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return str(self.reg_no)


class PriceChart(models.Model):
    vehicle_type= (
        ('SUV', 'SUV'),
        ('SEDAN', 'SEDAN'),
        ('BIKE', 'BIKE'),
        ('3-WHEELER','3-WHEELER'),
        ('TRUCK','TRUCK'),
        ('BUS','BUS')
        )
    vehicle_class= models.CharField(max_length=20,null=True, choices=vehicle_type)
    fitness_rate= models.CharField(max_length=20,null=True)
    taxtoken_rate= models.CharField(max_length=20,null=True)
    insurance_rate= models.CharField(max_length=20,null=True)
    color_rate= models.CharField(max_length=20,null=True)

    def __str__(self):
       return self.vehicle_class

class ManagedHistory(models.Model):
    vehicle_id = models.CharField(max_length=15,null=True)
    admin_id = models.CharField( max_length=11, null=True )
    date = models.DateTimeField(auto_now_add=True)