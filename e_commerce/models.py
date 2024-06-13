from django.db import models
import datetime
import os

def c_getfilename(request,filename):
    now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_filename='%s%s'%(now_time,filename)
    return os.path.join('e_commerce/catagory/',new_filename)

def p_getfilename(request,filename):
    now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_filename='%s%s'%(now_time,filename)
    return os.path.join('e_commerce/product/',new_filename)

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=150,null=False,blank=False)
    catagory_image = models.ImageField(upload_to=c_getfilename,null=True,blank=False) 
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-Hidden')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self .catagory_name
    
class Product(models.Model):
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=p_getfilename,null=True,blank=False) 
    quandity = models.PositiveIntegerField(null=False,blank=False)
    original_price = models.PositiveIntegerField(null=False,blank=False)
    selling_price = models.PositiveIntegerField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-Hidden')
    trending = models.BooleanField(default=False,help_text='0-default,1-Trending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self .product_name
