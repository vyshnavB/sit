from email.policy import default
from sre_constants import MAX_UNTIL
from statistics import mode
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload

from django.forms import CharField

# Create your models here.


class categories(models.Model):
     category_name=models.CharField(max_length=255,blank=True)  
     image=models.ImageField(upload_to='posts/', blank=True)   




class company(models.Model):
    category_name=models.ForeignKey(categories,related_name='cate',on_delete=models.CASCADE,blank=True,default=True)
    company_n=models.CharField(max_length=255,blank=True)  
    description=models.CharField(max_length=255,blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    company_image = models.FileField(upload_to='posts/', blank=True,null=True,)
    mobile=models.IntegerField(null=True,blank=True)
    alt_mobile=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=255,null=True,blank=True)
    web_link= models.URLField(blank=True, null=True)
    fb_link= models.URLField(blank=True, null=True)
    insta_link= models.URLField(blank=True, null=True)
    linkdin_link= models.URLField(blank=True, null=True)
    twit_link= models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    location_link = models.URLField(blank=True, null=True)
    service_1=models.CharField(max_length=255,null=True,blank=True)
    service_2=models.CharField(max_length=255,null=True,blank=True)
    service_3=models.CharField(max_length=255,null=True,blank=True)
    service_4=models.CharField(max_length=255,null=True,blank=True)
    service_5=models.CharField(max_length=255,null=True,blank=True)
    service_6=models.CharField(max_length=255,null=True,blank=True)
    service_7=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='posts/', blank=True)   
    image_2=models.ImageField(upload_to='posts/', blank=True)   
    image_3=models.ImageField(upload_to='posts/', blank=True)   
    image_4=models.ImageField(upload_to='posts/', blank=True)   
    image_5=models.ImageField(upload_to='posts/', blank=True)   
    image_6=models.ImageField(upload_to='posts/', blank=True)   
