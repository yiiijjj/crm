from django.db import models
from django.urls import reverse

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=16)
    zip = models.CharField(max_length=16)
    county = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state} {self.zip}, {self.county} County'

class BuildingType(models.Model):
    building_type = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('buildingtypedetail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.building_type

class Building(models.Model):
    building_type = models.ForeignKey(BuildingType, on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)

    def get_absolute_url(self):
        return reverse('buildingdetail',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.building_type)

class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    VIN = models.CharField(max_length=17, unique=True)

    def get_absolute_url(self):
        return reverse('vehicledetail',kwargs={'pk':self.pk})

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'

class PolicyType(models.Model):
    policy_type = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('policytypedetail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.policy_type

class Agency(models.Model):
    agency_name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)

    def get_absolute_url(self):
        return reverse('agencydetail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.agency_name

class Agent(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)

    def get_absolute_url(self):
        return reverse('agentdetail',kwargs={'pk':self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dob = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)

    def get_absolute_url(self):
        return reverse('customerdetail',kwargs={'pk':self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Policy(models.Model):
    policy_name = models.CharField(max_length=255)
    policy_type = models.ForeignKey(PolicyType, on_delete=models.RESTRICT)
    agency = models.ForeignKey(Agency, on_delete=models.RESTRICT)  # Assuming CASCADE is appropriate
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT)  # Assuming CASCADE is appropriate
    vehicle = models.ForeignKey(Vehicle, on_delete=models.RESTRICT)
    building = models.ForeignKey(Building, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policy')

    def get_absolute_url(self):
        return reverse('policydetail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.policy_name

class PolicyCustomer(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('policycustomerdetail',kwargs={'pk':self.pk})

    class Meta:
        unique_together = ('customer', 'policy')

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name}, {self.policy.policy_type}{self.policy.policy_name}'