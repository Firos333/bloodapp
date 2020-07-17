from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Donor_details,Request_details,Bloodbank

@admin.register(Donor_details)
class Donor_detailsAdmin(OSMGeoAdmin):
    list_display = ('email', 'location')

@admin.register(Request_details)
class Request_detailsAdmin(OSMGeoAdmin):
    list_display = ('Bloodgroup', 'location')

@admin.register(Bloodbank)
class BloodbankAdmin(OSMGeoAdmin):
    list_display = ('bloodbank_name', 'location')