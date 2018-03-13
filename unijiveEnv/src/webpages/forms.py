
from django import forms
from django.forms import formset_factory
from django.conf import settings  
from accounts.models import UserProfile
from django.forms.models import model_to_dict, fields_for_model
from django.contrib.auth.forms import UserCreationForm

User = settings.AUTH_USER_MODEL


'''
class UserCreateForm(forms.ModelForm):
    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('email', 'password',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(UserCreateForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))

    class Meta:
        model = UserProfile
        exclude = ('user','numberofLikes', 'profilePic')

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.firstName = self.cleaned_data['firstName']
        u.lastName = self.cleaned_data['lastName']
        u.username = self.cleaned_data['username']
        u.university = self.cleaned_data['university']
        u.password = self.cleaned_data['password']
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(UserCreateForm, self).save(*args,**kwargs)
        return profile

'''      

'''
class UserDetailsForm(ModelForm):
    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(UserDetailsForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))

    class Meta:
        model = UserDetails
        exclude = ('user',)

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(UserDetailsForm, self).save(*args,**kwargs)
        return profile
'''


'''
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

