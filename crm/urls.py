"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crmapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path('address/',views.AddressListView.as_view(),name='address'),
    path('<int:pk>/',views.AddressDetailView.as_view(),name='detail'),
    path('create/',views.AddressCreateView.as_view()),
    path('update/<int:pk>/',views.AddressUpdateView.as_view()),
    path('delete/<int:pk>/',views.AddressDeleteView.as_view()),
    path('buildingtype/',views.BuildingTypeListView.as_view(),name='buildingtype'),
    path('<int:pk>/',views.BuildingTypeDetailView.as_view(),name='buildingtypedetail'),
    path('buildingtypecreate/',views.BuildingTypeCreateView.as_view()),
    path('buildingtypeupdate/<int:pk>/',views.BuildingTypeUpdateView.as_view()),
    path('buildingtypedelete/<int:pk>/',views.BuildingTypeDeleteView.as_view()),
    path('building/',views.BuildingListView.as_view(),name='building'),
    path('<int:pk>/',views.BuildingDetailView.as_view(),name='buildingdetail'),
    path('buildingcreate/',views.BuildingCreateView.as_view()),
    path('buildingupdate/<int:pk>/',views.BuildingUpdateView.as_view()),
    path('buildingdelete/<int:pk>/',views.BuildingDeleteView.as_view()),
    path('vehicle/',views.VehicleListView.as_view(),name='vehicle'),
    path('<int:pk>/',views.VehicleDetailView.as_view(),name='vehicledetail'),
    path('vehiclecreate/',views.VehicleCreateView.as_view()),
    path('vehicleupdate/<int:pk>/',views.VehicleUpdateView.as_view()),
    path('vehicledelete/<int:pk>/',views.VehicleDeleteView.as_view()),
    path('policytype/',views.PolicyTypeListView.as_view(),name='policytype'),
    path('<int:pk>/',views.PolicyTypeDetailView.as_view(),name='policytypedetail'),
    path('policytypecreate/',views.PolicyTypeCreateView.as_view()),
    path('policytypeupdate/<int:pk>/',views.PolicyTypeUpdateView.as_view()),
    path('policytypedelete/<int:pk>/',views.PolicyTypeDeleteView.as_view()),
    path('agency/',views.AgencyListView.as_view(),name='agency'),
    path('<int:pk>/',views.AgencyDetailView.as_view(),name='agencydetail'),
    path('agencycreate/',views.AgencyCreateView.as_view()),
    path('agencyupdate/<int:pk>/',views.AgencyUpdateView.as_view()),
    path('agencydelete/<int:pk>/',views.AgencyDeleteView.as_view()),
    path('agent/',views.AgentListView.as_view(),name='agent'),
    path('<int:pk>/',views.AgentDetailView.as_view(),name='agentdetail'),
    path('agentcreate/',views.AgentCreateView.as_view()),
    path('agentupdate/<int:pk>/',views.AgentUpdateView.as_view()),
    path('agentdelete/<int:pk>/',views.AgentDeleteView.as_view()),
    path('customer/',views.CustomerListView.as_view(),name='customer'),
    path('<int:pk>/',views.CustomerDetailView.as_view(),name='customerdetail'),
    path('customercreate/',views.CustomerCreateView.as_view()),
    path('customerupdate/<int:pk>/',views.CustomerUpdateView.as_view()),
    path('customerdelete/<int:pk>/',views.CustomerDeleteView.as_view()),
    path('policy/',views.PolicyListView.as_view(),name='policy'),
    path('<int:pk>/',views.PolicyDetailView.as_view(),name='policydetail'),
    path('policycreate/',views.PolicyCreateView.as_view()),
    path('policyupdate/<int:pk>/',views.PolicyUpdateView.as_view()),
    path('policydelete/<int:pk>/',views.PolicyDeleteView.as_view()),
    path('policycustomer/',views.PolicyCustomerListView.as_view(),name='policycustomer'),
    path('<int:pk>/',views.PolicyCustomerDetailView.as_view(),name='policycustomerdetail'),
    path('policycustomercreate/',views.PolicyCustomerCreateView.as_view()),
    path('policycustomerupdate/<int:pk>/',views.PolicyCustomerUpdateView.as_view()),
    path('policycustomerdelete/<int:pk>/',views.PolicyCustomerDeleteView.as_view()),
]
