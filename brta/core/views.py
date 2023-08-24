from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, VehicleForm, UpdateRecordForm
from .models import User, Vehicle_fixed_detail, Vehicle_variable_details, PriceChart, ManagedHistory

# Create your views here.

def home(request):


    if request.method == 'POST':
        userId =  request.POST['userId']
        password = request.POST['password']

        #Authentication
        user = authenticate(request, username=userId, password= password)
        vehicles= Vehicle_fixed_detail.objects.all()
        if user is not None:
            login(request, user)

            if user.is_staff== True:
        
                messages.success(request, "Welcome Mr. Admin!")
                return render(request, 'home.html', {'vehicles':vehicles})
            elif user.is_staff== False:
                #Model.objects.filter(field_name=some_param)
                messages.success(request, f"Welcome Mr./Ms. {user.name}")
                vehicle = Vehicle_fixed_detail.objects.filter(client_id=user.license_no)
                return render(request, 'home.html', {'vehicles':vehicle})


                
            messages.success(request, 'Successfully Logged In!')
            return render(request, 'home.html', {})
        else:
            messages.success(request, "LogIn Failed...!!!")
            return render(request, 'home.html', {})
    elif request.user.is_authenticated:
        if request.user.is_staff== True:
                vehicles= Vehicle_fixed_detail.objects.all()
                return render(request, 'home.html', {'vehicles':vehicles})
        elif request.user.is_staff== False:
                vehicle = Vehicle_fixed_detail.objects.filter(client_id=request.user.license_no)
                return render(request, 'home.html', {'vehicles':vehicle})
    else:
        return render(request, 'home.html', {})

        
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged Out !!!")
    return redirect('home')


def register_user(request):

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST.get('license_no')
            user.user_id = request.POST.get('license_no')
            user.save()
            
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
   
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

def register_vehicle(request):

    if request.user.is_staff== True:

        vform = VehicleForm()
        
        if request.method == 'POST':
            vform = VehicleForm(request.POST)
            
            if vform.is_valid():
                vehicle = vform.save(commit=False)
                vehicle.save()
            
                Vehicle_variable_details.objects.create(
                reg_no=vehicle,
            )
            messages.success(request, 'Successfully Registered the Vehicle!')
            return redirect('home')
        else:
            vform = VehicleForm()
            return render(request, 'register-vehicle.html', {'form':vform})
    return render(request, 'register-vehicle.html', {'form':vform})



def vehicle_variable_details(request, pk):
    if request.user.is_authenticated:
        user = Vehicle_fixed_detail.objects.get(id=pk)
        price_chart= PriceChart.objects.get(vehicle_class= user.vehicle_class)
        client = User.objects.filter(license_no = user.client_id)
        if len(client)==0:
             client=[   'Still not Registered in database'  ]
		# Look Up Records
        vehicle_record = Vehicle_variable_details.objects.get(reg_no=pk)

        if request.method == 'POST':
            dic=request.POST.dict()
            if vehicle_record.request_with_payment!= None:
                 old= vehicle_record.request_with_payment+'\n'
            else:
                 old=""
            # += request.POST['message']+'-'+request.POST['color']+'\n'
            if dic.get('fitness')!= None:
                 old += 'Paid:'+dic.get('fitness')+'--Update Fitness(1year)<br> '
            if dic.get('taxtoken')!= None:
                 old += 'Paid:'+dic.get('taxtoken')+'--Update taxtoken(1year)<br>'
            if dic.get('insurance')!= None:
                 old += 'Paid:'+dic.get('insurance')+'--Update insurance(1year)<br>'
            if dic.get('color')!= None:
                 old += 'Paid:'+dic.get('color')+'--Change Color to-['+dic.get('message')+']<br>'

            vehicle_record.request_with_payment = old
            vehicle_record.save()
            
            return render(request, 'vehicle_details.html', {'vehicle_record':vehicle_record,'client':client[0],'price_chart':price_chart})
        else:
             
            return render(request, 'vehicle_details.html', {'vehicle_record':vehicle_record,'client':client[0],'price_chart':price_chart})
    
        
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Vehicle_fixed_detail.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')



def update_record(request,pk):
     if request.user.is_authenticated:
          current_record = Vehicle_variable_details.objects.get(reg_no=pk)
          form = UpdateRecordForm(request.POST or None, instance=current_record)
          if form.is_valid():
               form.save()
               ManagedHistory.objects.create(
                    vehicle_id = current_record.reg_no,
                    admin_id = request.user.user_id,
               )
               messages.success(request, "Record Has Been Updated!")
               return redirect('all-request')
          else:
               return render(request, 'update_record.html', {'form':form})
     else:
          messages.success(request, "You Must Be Logged In...")
          return redirect('home')
          
               

def client_details(request,pk):
     
     client = User.objects.filter(license_no = pk)
     if len(client)==0:
          client=[   {'name':'Client Still not Registered in database'}  ]
             
     return render(request, 'client_details.html', {'client':client[0]})


def all_request(request):
     if request.user.is_authenticated:
        # user = Vehicle_fixed_detail.objects.get(id=pk)
        vehicles = Vehicle_variable_details.objects.exclude(request_with_payment__iexact=None)


        return render(request, 'all-request.html',{'vehicles': vehicles})
     else:
          return render(request, 'all-request.html')