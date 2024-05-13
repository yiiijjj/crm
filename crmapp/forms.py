from django import forms
from crmapp.models import Address,BuildingType,Building,Vehicle,PolicyType,Agency,Agent,Customer,Policy,PolicyCustomer

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class BuildingTypeForm(forms.ModelForm):
    class Meta:
        model = BuildingType
        fields = '__all__'

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class PolicyTypeForm(forms.ModelForm):
    class Meta:
        model = PolicyType
        fields = '__all__'

class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = '__all__'

class PolicyCustomerForm(forms.ModelForm):
    class Meta:
        model = PolicyCustomer
        fields = '__all__'