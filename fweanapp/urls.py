from django.urls import path

from .views import *
from django.conf.urls import handler404

app_name = "fweanapp"

urlpatterns = [

path('admin-home/',AdminDashboardView.as_view(), name = 'admindashboard' ),


path('admin/organization/create/', AdminOrganizationCreateView.as_view(), name = 'adminorganizationcreate'),
path('admin/organization/update/<int:pk>/', AdminOrganizationUpdateView.as_view(), name = 'adminorganizationupdate'),
path('admin/organization/detail/<int:pk>/', AdminOrganizationDetailView.as_view(), name = 'adminorganizationdetail'),





path('',ClientIndexView.as_view(), name = 'indexpage' ),
path('contact-us/',ClientContactUsView.as_view(), name = 'clientcontactus' ),

]