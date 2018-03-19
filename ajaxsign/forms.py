from django import forms
from .models import Sign




class ProfileForm(forms.Form):
   prrofile_picture = forms.ImageField()

   class Meta:
       Sign = "profile"