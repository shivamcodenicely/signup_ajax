from django.db import models
import jsonfield


# Create your models here.
class Sign(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, primary_key=True)
    contact = models.IntegerField(default=0)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='')

    def __str__(self):
        return self.fname

class Otp_match(models.Model):
    user=models.ForeignKey(Sign,on_delete=models.CASCADE)
    otp=models.IntegerField(default=0)
    status=models.BooleanField(default=False)

class Electonics(models.Model):
    id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=256)
    def __str__(self):
        return self.product_name


class Mobiles(models.Model):
    mobile_user=models.ForeignKey(Electonics,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    brand_name=models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name

class Mobile_Brand(models.Model):
    mobile_brand_user=models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    model_name=models.CharField(max_length=20)
    def __str__(self):
        return self.model_name

class Mobile_Model(models.Model):
    mobile_model_detail=models.ForeignKey(Mobile_Brand,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    model_number=models.CharField(max_length=20)
    price=models.IntegerField(null=False,blank=False)
    description=models.CharField(max_length=300)
    def __str__(self):
        return self.model_number

class Laptops(models.Model):
    laptop_user=models.ForeignKey(Electonics,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    brand_name=models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name

class Laptop_Brand(models.Model):
    laptop_brand_user=models.ForeignKey(Laptops,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    brand_name=models.CharField(max_length=20)
    def __str__(self):
        return self.brand_name

class Laptop_Model(models.Model):
    laptop_model_detail=models.ForeignKey(Laptop_Brand,on_delete=models.CASCADE)
    id=models.IntegerField(primary_key=True)
    model_number=models.CharField(max_length=20)
    price=models.IntegerField(null=False,blank=False)
    description=models.CharField(max_length=300)
    def __str__(self):
        return self.model_number







