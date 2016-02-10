from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Password",
    widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",
    widget=forms.PasswordInput)
    error_messages= {'password_mismatch': 'passwords not match'}

    class Meta:
        model = User
        fields = ('email','last_name', 'first_name', 'username')


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

