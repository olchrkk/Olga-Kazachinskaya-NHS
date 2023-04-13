from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = User
        fields = 'email'

    def clean_password(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords didn't match")
        return data['password2']