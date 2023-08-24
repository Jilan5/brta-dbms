from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add-vehicle/',views.register_vehicle, name='register-vehicle'),
    path('vehicle-details/<str:pk>',views.vehicle_variable_details, name='vehicle-details'),
    path('delete_record/<str:pk>', views.delete_record, name='delete_record'),
    path('update_record/<str:pk>', views.update_record, name='update_record'),
    path('client-details/<str:pk>',views.client_details, name='client-details'),
    path('all-request/', views.all_request, name='all-request'),
    
]