from django.shortcuts import render,redirect
from crmapp.models import Address,BuildingType,Building,Vehicle,PolicyType,Agency,Agent,Customer,Policy,PolicyCustomer
from crmapp.forms import AddressForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'crmapp/index.html')

class AddressListView(ListView):
    model = Address

class AddressDetailView(DetailView):
    model = Address

class AddressCreateView(CreateView):
    model = Address
    fields = ('street','city','state','zip','county')

class AddressUpdateView(UpdateView):
    model = Address
    fields = ('street','city','state','zip','county')

class AddressDeleteView(DeleteView):
    model = Address
    success_url = reverse_lazy('address')

class BuildingTypeListView(ListView):
    model = BuildingType

class BuildingTypeDetailView(DetailView):
    model = BuildingType

class BuildingTypeCreateView(CreateView):
    model = BuildingType
    fields = ('building_type',)

class BuildingTypeUpdateView(UpdateView):
    model = BuildingType
    fields = ('building_type',)

class BuildingTypeDeleteView(DeleteView):
    model = BuildingType
    success_url = reverse_lazy('buildingtype')

class BuildingListView(ListView):
    model = Building

class BuildingDetailView(DetailView):
    model = Building

class BuildingCreateView(CreateView):
    model = Building
    fields = ('building_type','address')

class BuildingUpdateView(UpdateView):
    model = Building
    fields = ('building_type','address')

class BuildingDeleteView(DeleteView):
    model = Building
    success_url = reverse_lazy('building')

class VehicleListView(ListView):
    model = Vehicle

class VehicleDetailView(DetailView):
    model = Vehicle

class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ('year','make', 'model', 'VIN')

class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ('year','make', 'model', 'VIN')

class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle')

class PolicyTypeListView(ListView):
    model = PolicyType

class PolicyTypeDetailView(DetailView):
    model = PolicyType

class PolicyTypeCreateView(CreateView):
    model = PolicyType
    fields = ('policy_type',)

class PolicyTypeUpdateView(UpdateView):
    model = PolicyType
    fields = ('policy_type',)

class PolicyTypeDeleteView(DeleteView):
    model = PolicyType
    success_url = reverse_lazy('policytype')

class AgencyListView(ListView):
    model = Agency

class AgencyDetailView(DetailView):
    model = Agency

class AgencyCreateView(CreateView):
    model = Agency
    fields = ('agency_name','address')

class AgencyUpdateView(UpdateView):
    model = Agency
    fields = ('agency_name','address')

class AgencyDeleteView(DeleteView):
    model = Agency
    success_url = reverse_lazy('agency')

class AgentListView(ListView):
    model = Agent

class AgentDetailView(DetailView):
    model = Agent

class AgentCreateView(CreateView):
    model = Agent
    fields = ('first_name','last_name','address','phone','email')

class AgentUpdateView(UpdateView):
    model = Agent
    fields = ('first_name','last_name','address','phone','email')

class AgentDeleteView(DeleteView):
    model = Agent
    success_url = reverse_lazy('agent')

class CustomerListView(ListView):
    model = Customer

class CustomerDetailView(DetailView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    fields = ('first_name','last_name','dob','address','phone','email')

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ('first_name','last_name','dob','address','phone','email')

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer')

class PolicyListView(ListView):
    model = Policy

class PolicyDetailView(DetailView):
    model = Policy

class PolicyCreateView(CreateView):
    model = Policy
    fields = ('policy_name','policy_type','agency','agent','vehicle','building','customer')

class PolicyUpdateView(UpdateView):
    model = Policy
    fields = ('policy_name','policy_type','agency','agent','vehicle','building','customer')

class PolicyDeleteView(DeleteView):
    model = Policy
    success_url = reverse_lazy('policy')

class PolicyCustomerListView(ListView):
    model = PolicyCustomer

class PolicyCustomerDetailView(DetailView):
    model = PolicyCustomer

class PolicyCustomerCreateView(CreateView):
    model = PolicyCustomer
    fields = ('policy','customer')

class PolicyCustomerUpdateView(UpdateView):
    model = PolicyCustomer
    fields = ('policy','customer')

class PolicyCustomerDeleteView(DeleteView):
    model = PolicyCustomer
    success_url = reverse_lazy('policycustomerdetail')