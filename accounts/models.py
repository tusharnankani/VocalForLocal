from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):

  phone = models.CharField(max_length=10)
  pincode = models.CharField(max_length=6)  

class Tag(models.Model) : 
  name = models.CharField(max_length = 50)

  def __str__(self) : 
    return self.name

class Seller(models.Model):

  shop_name = models.CharField(max_length=50)
  shop_owner = models.CharField(max_length=50)  
  address = models.CharField(max_length=80)  
  phone = models.CharField(max_length=10)
  pincode = models.CharField(max_length=6)
  category = models.CharField(max_length=20)
  time = models.CharField(max_length=10)
  tags = models.ManyToManyField(Tag, blank = True)

  def __str__(self):
    return self.shop_name


 
  