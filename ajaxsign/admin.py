from django.contrib import admin

from ajaxsign.models import Sign,Otp_match,Electonics,Mobiles,Mobile_Brand,Mobile_Model,Laptop_Brand,Laptop_Model,Laptops
mymodels=[Sign,Otp_match,Electonics,Mobiles,Mobile_Brand,Mobile_Model,Laptop_Brand,Laptop_Model,Laptops]

admin.site.register(mymodels)

