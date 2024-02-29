from django.db import models
from django.forms import ModelForm

# Create your models here.

class reg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class maincategory(models.Model):
    category = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

class subcategory(models.Model):
    userid = models.IntegerField(default=0)
    subitem = models.CharField(max_length=100,default=0)
    item = models.CharField(max_length=100)

      
class productdata(models.Model):
    pcatagory = models.CharField(max_length=100)
    psubcatagory = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    pstatus = models.IntegerField(default=0)
    image = models.FileField(upload_to='media/')

class imagedata(ModelForm):
    class Meta:
        model = productdata
        fields = ['pcatagory','psubcatagory','name','discription','price','quantity','discount','pstatus','image']