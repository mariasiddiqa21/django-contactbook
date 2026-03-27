from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
import re



# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=100,blank=False)
  email = models.EmailField(max_length=100,blank=False)
  phone = models.CharField(max_length=100,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
  
  def clean(self):
        if not self.name.isalpha():
            raise ValidationError("Name must contain only letters")
        if not re.match(r'^\d{10}$', self.phone):
            raise ValidationError("Phone number must be 10 digits")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
            raise ValidationError("Invalid email format")
  
  
  def __str__(self):
    return self.name  