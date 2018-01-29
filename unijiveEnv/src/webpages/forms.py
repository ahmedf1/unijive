
from django import forms
from django.conf import settings  
from accounts.models import UserProfile
User = settings.AUTH_USER_MODEL


class UserCreateForm(forms.ModelForm):
    class Meta:
        model   = UserProfile
        fields  = [
            'firstName',
            'lastName',
            'university',
            #'email',
            'username',
            #'password',
        ]
'''
    def clean_email(self):
        email   = self.cleaned_data.get("email")
        if ".edu" not in email:
            raise forms.ValidationError("Please use your University associated email")
        return email
'''

