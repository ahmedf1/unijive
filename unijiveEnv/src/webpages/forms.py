
from django import forms
from django.forms import formset_factory
from django.conf import settings  
from accounts.models import UserProfile
User = settings.AUTH_USER_MODEL


class UserProfileCreateForm(forms.ModelForm):
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
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]



UserInLineFormset = formset_factory(
    UserProfile,
    User,
    form = UserProfileCreateForm,
    extra = 1,
    can_delete = False,
    can_order = False
)
'''








'''
    def clean_email(self):
        email   = self.cleaned_data.get("email")
        if ".edu" not in email:
            raise forms.ValidationError("Please use your University associated email")
        return email
'''

