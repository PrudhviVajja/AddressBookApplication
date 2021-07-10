from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    address = models.CharField(max_length=255, verbose_name="Address", blank=True)
    email = models.EmailField(max_length=50, verbose_name="Email", blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Correct format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Phone Number") # validators should be a list
    date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    
    def __str__(self,):
        return self.first_name + self.last_name
    
    class Meta:
        ordering = ['first_name']