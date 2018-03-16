from django.db import models



# Create your models here.
class Sign(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, primary_key=True)
    contact = models.CharField(max_length=50)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='')

    def __str__(self):
        return self.fname

class Otp_match(models.Model):
    user=models.ForeignKey(Sign,on_delete=models.CASCADE)
    otp=models.IntegerField(default=0)
    status=models.BooleanField(default=False)

