
from django import forms
#from .models import UserZ
'''
class UserCreateForm(forms.ModelForm):
    class Meta:
        model   = UserZ
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
'''
