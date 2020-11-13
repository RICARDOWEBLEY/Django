from . import views 
from django.urls import path
from  .views import *
from asset.views import view_by_location
from django.contrib.auth import views as auth_views



urlpatterns = [
   # path('dashboard/', views.asset, name='asset'),
    path('acquisition/', AcquisitionCreateView.as_view(), name='acquisition'),
    path('view_acquisition/', AcquisitionListView.as_view(), name='view_acquisition'),
    path('update_acquisition/<str:pk>/', AcquisitionUpdateView.as_view(), name='update_acquisition'),
    path('acquisition_detail/<str:pk>/', AcquisitionDetailView.as_view(), name='acquisition_detail'),


    path('view_manufacturer/', ManufacturerListView.as_view(), name='view_manufacturer'),
    path('view_department/', DepartmentListView.as_view(), name='view_department'),
    path('transfers/' , TransferCreateView.as_view(), name='transfers'),
    path('view-transfer/', TransferListView.as_view(), name='view-transfer'),
    path('update-transfer/<str:pk>/', TransferUpdateView.as_view(), name='update-transfer'),
    path('written-off/', WrittenoffListView.as_view(), name='written-off'),
    path('view-users/', views.viewusers, name='view-users'),
    path('view-by-location/<str:location_id>/', views.view_by_location, name='view-by-location'),
    path('view-by-department/<str:dept_id>/', views.view_by_department, name='view-by-department'),


]