  
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MY_Type = (
        ('Regular', 'Regular'),
        ('Square', 'Square'),
    )
class PizzaToppings(models.Model):
    Name=models.CharField(null=True,blank=True,max_length=15)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.Name

MY_Size = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )


class Pizza(models.Model):
    Pizza_type=models.CharField(max_length=15,null=True,blank=True,default=None,choices=MY_Type)
    Pizza_toppings=models.ManyToManyField(PizzaToppings)
    Pizza_Size=models.CharField(max_length=15,null=True,blank=True,default=None,choices=MY_Size)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='CreateBy')
    UpdateBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='UpdateBy')
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)