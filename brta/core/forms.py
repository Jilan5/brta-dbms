from django.forms import ModelForm
from .models import User, Region, Vehicle_fixed_detail, Vehicle_variable_details
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model= User
        fields=['name','license_no','addr', 'nid','date_of_birth','blood_group','driver_class','region_id','password1','password2']
        exclude= []

class VehicleForm(ModelForm):

    class Meta:
        model= Vehicle_fixed_detail
        fields = ['client_id','engine_no','seat','fuel_type','engine_cc','vehicle_class']
        exclude= []

class UpdateRecordForm(ModelForm):

    class Meta:
        model = Vehicle_variable_details
        fields = '__all__'
        exclude=['reg_no']