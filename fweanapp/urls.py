from django.urls import path

from .views import *
from django.conf.urls import handler404

app_name = "fweanapp"

urlpatterns = [

path('admin-dashboard/',AdminDashboardView.as_view(), name = 'admindashboard' ),


path('admin/organization/create/', AdminOrganizationCreateView.as_view(), name = 'adminorganizationcreate'),
path('admin/organization/update/<int:pk>/', AdminOrganizationUpdateView.as_view(), name = 'adminorganizationupdate'),
path('admin/organization/detail/<int:pk>/', AdminOrganizationDetailView.as_view(), name = 'adminorganizationdetail'),


path('admin/image-album/add/', ImageAlbumAddView.as_view(), name = 'imagealbumadd'),
path('admin/imagealbum/list/', ImageAlbumListView.as_view(), name = 'imagealbumlist'),
# path('admin/imagealbum/<int:pk>/detail/', ImageAlbumDetailView.as_view(), name = 'adminimagealbumdetail'),
# path('admin/imagealbum/<int:pk>/update/', ImageAlbumUpdateView.as_view(), name = 'adminimagealbumupdate'),
# path('admin/imagealbum/<int:pk>/delete/', ImageAlbumDeleteView.as_view(), name = 'adminimagealbumdelete'),



path('',ClientIndexView.as_view(), name = 'indexpage' ),
path('contact-us/',ClientContactUsView.as_view(), name = 'clientcontactus' ),

]