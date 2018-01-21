from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager )

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''
Super User Login Info  (Move from here after viewing)
   email : farhad@sucks.com
    pass : king123456

'''


class UserManager(BaseUserManager):
    def create_user(self, email, password = None, is_active = True, is_staff = False, is_admin = False):
        if not email: raise ValueError("Users must have an email address! ")
        if not password: raise ValueError("Users must have a password! ")
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff  = is_staff
        user_obj.admin  = is_admin
        user_obj.save(using=self.db)
        return user_obj

    def create_staffuser(self, email, password = None):
        user_obj = self.create_user(email, password=password, is_staff =True)
        return user_obj

    def create_superuser(self, email, password = None):
        user_obj = self.create_user(email, password=password, is_staff =True, is_admin = True)
        return user_obj



#customUser not standard djano User class
class User(AbstractBaseUser):
    email           = models.EmailField(max_length= 255, unique =True)
    active          = models.BooleanField(default= True)
    staff           = models.BooleanField(default = False)
    admin           = models.BooleanField(default = False)
    memberSince     = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def _str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        #"Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        #"Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        #"Is the user active?"
        return self.active


class UserProfile(models.Model):
    user            = models.OneToOneField(User)
    firstName       = models.CharField(max_length = 30)
    lastName        = models.CharField(max_length = 30)
    username        = models.CharField(max_length = 30)
    university      = models.CharField(max_length = 30)
    numberofLikes   = models.IntegerField(default = 0)
    profilePic      = models.ImageField(default = os.path.join(BASE_DIR, "/webpages/static/icons_/account_icon.PNG") )
    
    YEAR_IN_SCHOOL_CHOICES = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    )
    year_in_school = models.CharField(max_length=15, choices=YEAR_IN_SCHOOL_CHOICES, default='Freshman',)
    
    #def get_full_name(self):
        # The user is identified by their email address
        #return self.firstName + " " + self.lastName
