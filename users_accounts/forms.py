from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
   password1 = forms.CharField(label="Password",
   widget=forms.PasswordInput)
   password2 = forms.CharField(label="Confirm Password",
   widget=forms.PasswordInput)
                
   class Meta:
       model = User
       fields = ('email','last_name', 'first_name')
