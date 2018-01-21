
from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = [
            'firstName',
            'lastName',
            'university',
            'email',
            'password',
            'username',
        ]

    def clean_email(self):
        email   = self.cleaned_data.get("email")
        if ".edu" not in email:
            raise forms.ValidationError("Please use your University associated email")
        return email

