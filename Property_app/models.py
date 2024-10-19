from django.db import models

# Create your models here.

property_types =(
    'Apartment','apartment'
    'House','house'
    'Commercial','commercial'

)


class Property(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Description = models.TextField()
    Number_of_units = models.IntegerField()

    def __str__(self):
        return f'{self.Name} is located in {self.Address}'


class Units(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    Unit = models.IntegerField()
    Bedrooms = models.IntegerField()
    Bathrooms = models.IntegerField()
    Rent = models.IntegerField()
    Is_Available = models.BooleanField()
    def __str__(self):
        return f'{self.Unit} {self.Bedrooms} {self.Bathrooms} {self.Rent} {self.Is_Available}'

class Tenant (models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=14)
    def __str__(self):
        return f'{self.Name}  {self.Email}  {self.Phone_number}'



class Lease(models.Model):
    Tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE)
    unit = models.ForeignKey(Units,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    Rent_amount = models.IntegerField()
    def __str__(self):
        return f'{self.Tenant} {self.unit} {self.start_date} {self.end_date}{self.Rent_amount}'





