from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DeleteView, UpdateView, CreateView, DetailView
)
from .models import Acquisition, Manufacturer, Department, Location, Transfer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def viewusers(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'asset/view-users.html', context)


class AcquisitionCreateView(LoginRequiredMixin, CreateView):
    model = Acquisition
    template_name = 'asset/acquisition_form.html'
    fields = ['asset_name', 'asset_number', 'serial_number', 'manufacturer', 'model', 'purchased_from', 'notes']

    def form_valid(self, form):
        form.instance.post_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AcquisitionCreateView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'New Acquisition'
        return context


class AcquisitionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Acquisition
    template_name = 'asset/acquisition_form.html'
    fields = ['asset_name', 'asset_number', 'serial_number', 'manufacturer', 'model', 'purchased_from', 'notes']

    def test_func(self):
        acquisition = self.get_object()
        if self.request.user == acquisition.post_by:
            return True
        return False


class AcquisitionDetailView(LoginRequiredMixin, DetailView):
    model = Acquisition

    def get_context_data(self, **kwargs):
        context = super(AcquisitionDetailView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'Acquisition Details'
        return context


class AcquisitionListView(LoginRequiredMixin, ListView):
    model = Acquisition
    queryset = Acquisition.objects.all()
    context_object_name = 'acquisitions'
    ordering = ['-date_acquired']
    template_name = 'asset/acquisition_view.html'

    def get_context_data(self, **kwargs):
        context = super(AcquisitionListView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'Acquisitions'
        return context


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all()
    context_object_name = 'manufacturers'
    ordering = ['manufacturer_name']
    template_name = 'asset/manufacturer_view.html'

    def get_context_data(self, **kwargs):
        context = super(ManufacturerListView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'Manufacturers'
        return context


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    queryset = Department.objects.all()
    context_object_name = 'departments'
    # ordering = ['manufacturer_name']
    template_name = 'asset/department_view.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'Departments'
        return context


class TransferCreateView(LoginRequiredMixin, CreateView):
    model = Transfer
    template_name = 'asset/transfer_form.html'

    fields = ['asset', 'assigned_to', 'department_assigned', 'location_assigned', 'is_active']

    def get_context_data(self, **kwargs):
        context = super(TransferCreateView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'New Transfer'
        return context


class TransferListView(LoginRequiredMixin, ListView):
    model = Transfer
    queryset = Transfer.objects.filter(is_active=True).all()
    context_object_name = 'transfers'
    ordering = ['-date_transferred']
    template_name = 'asset/transfer_view.html'

    def get_context_data(self, **kwargs):
        context = super(TransferListView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'All Transfers'
        return context


class TransferUpdateView(LoginRequiredMixin, UpdateView):
    model = Transfer
    template_name = 'asset/update_acquistion.html'
    fields = ['asset', 'assigned_to', 'department_assigned', 'location_assigned', 'is_active']

    def get_context_data(self, **kwargs):
        context = super(TransferUpdateView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'Update Transfers'
        return context


class WrittenoffListView(LoginRequiredMixin, ListView):
    model = Transfer
    queryset = Transfer.objects.filter(is_active=False)
    context_object_name = 'transfers'
    template_name = 'asset/writtenoff.html'

    def get_context_data(self, **kwargs):
        context = super(WrittenoffListView, self).get_context_data(**kwargs)
        # Add context data to pass to template
        context['title'] = 'Board of Servey'
        return context


@login_required(login_url='login')
def view_by_location(request, location_id):
    location = Location.objects.get(pk=location_id)
    context = {'location': location}
    return render(request, 'asset/location_cat_view.html', context)


@login_required(login_url='login')
def view_by_department(request, dept_id):
    department = Department.objects.get(pk=dept_id)
    context = {'department': department}
    return render(request, 'asset/department_cat_view.html', context)
