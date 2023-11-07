from django.contrib import admin
from .models import Trains

# Register your models here.
class TrainAdministrator(admin.AdminSite):
    site_header = 'Train Administrator'
    site_title = 'Manage Trains'  
    index_title = 'Dashboard'


    
Train_Admin = TrainAdministrator(name = 'TrainAdmin')

Train_Admin.register(Trains)


