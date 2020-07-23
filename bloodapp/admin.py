from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Donor_details,Request_details

@admin.register(Donor_details)
class Donor_detailsAdmin(OSMGeoAdmin):
    list_display = ('email', 'location')

@admin.register(Request_details)
class Request_detailsAdmin(OSMGeoAdmin):
    list_display = ('Bloodgroup', 'location')

# @admin.register(Bloodbank)
# class BloodbankAdmin(OSMGeoAdmin):
#     list_display = ('bloodbank_name', 'location')

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','bloodbank_name','address','phone')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)