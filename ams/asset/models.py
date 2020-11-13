from django.db import models
from django.db.models.signals import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(unique=True, max_length=200, null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['manufacturer_name']

    def __str__(self):
        return self.manufacturer_name


class Acquisition(models.Model):
    asset_name = models.CharField(max_length=200, default=None)
    asset_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
    serial_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=200, null=True, blank=True)
    purchased_from = models.CharField(max_length=200, null=True, blank=True)
    date_acquired = models.DateTimeField(default=timezone.now, null=True, blank=True)
    post_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        ordering = ['date_acquired']

    def __str__(self):
        #return "%s The Asset is " % self.asset_name
        return self.asset_name

    def get_absolute_url(self):
        return reverse('acquisition_detail', kwargs={'pk': self.pk})


class Department(models.Model):
    department_name = models.CharField(unique=True, max_length=200, null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['department_name']

    def __str__(self):
        return self.department_name


class Location(models.Model):
    location_name = models.CharField(unique=True, max_length=200, null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['location_name']

    def __str__(self):
        return self.location_name

    #def get_absolute_url(self):
        #return reverse('location_view')


class Transfer(models.Model):
    asset = models.OneToOneField(Acquisition, default=None, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=200, null=True, blank=False)
    department_assigned = models.ForeignKey(Department, on_delete=models.CASCADE)
    location_assigned = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_transferred = models.DateTimeField(default=timezone.now, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_transferred']

    def __str__(self):
        return  self.assigned_to + ' - ' + str(self.asset)
        #return "%s The Asset is " % self.asset_name

    def get_absolute_url(self):
        return reverse('view-transfer')
