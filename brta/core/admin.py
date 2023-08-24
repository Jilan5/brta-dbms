from django.contrib import admin

# Register your models here.
from .models import User, Vehicle_fixed_detail, Region, Vehicle_variable_details, PriceChart

admin.site.register(User)
admin.site.register(Vehicle_fixed_detail)
admin.site.register(Region)
admin.site.register(Vehicle_variable_details)
admin.site.register(PriceChart)