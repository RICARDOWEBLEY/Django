from django.contrib import admin

from . models import *

#admin.site.register(Transfer)
#admin.site.register(Location)
  




class AcquisitionAdmin(admin.ModelAdmin):
    list_display =('asset_name', 'asset_number', 'serial_number', 'manufacturer', 'model', 'purchased_from', 'date_acquired','active')
    list_filter = ['asset_number', 'asset_name']
    search_fields = ['asset_name', 'asset_number']
admin.site.register(Acquisition, AcquisitionAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer_name', 'description')
    search_fields = ['manufacturer_name']
    list_filter = ['manufacturer_name']
admin.site.register(Manufacturer, ManufacturerAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'description')
    search_fields = ['department_name']
    list_filter = ['department_name']
admin.site.register(Department, DepartmentAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'description')
    search_fields = ['location_name']
    list_filter = ['location_name']
admin.site.register(Location, LocationAdmin)


class TransferAdmin(admin.ModelAdmin):
    list_display =('asset', 'assigned_to', 'department_assigned', 'location_assigned', 'date_transferred', 'is_active')
    list_filter = ['asset', 'assigned_to']
    search_fields = ['asset', 'assigned_to']
admin.site.register(Transfer, TransferAdmin)