from django.db import models
from django.conf import settings            #importing base.py
import os

from accounts.models import User
#User = settings.AUTH_USER_MODEL
 
# Create your models here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)
#print(os.path.join(BASE_DIR, "/webpages/static/icons_/account_icon.PNG"))

'''
class UserZ(models.Model):
    class Meta:
        verbose_name_plural = "Users"
    userID          = models.AutoField(primary_key=True)
    email           = models.EmailField(default = "USSALEXISTEXS@PORNHUB.COM")
    username        = models.CharField(max_length = 30)
    university      = models.CharField(max_length = 30)
    firstName       = models.CharField(max_length = 30)
    lastName        = models.CharField(max_length = 30)
    memberSince     = models.DateTimeField(auto_now_add=True)
    numberofLikes   = models.IntegerField(default = 0)
    password        = models.CharField(max_length = 20)  #ADD VALIDATORS
    profilePic      = models.ImageField(default = os.path.join(BASE_DIR, "/webpages/static/icons_/account_icon.PNG") )
 
    YEAR_IN_SCHOOL_CHOICES = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    )
    year_in_school = models.CharField(max_length=15, choices=YEAR_IN_SCHOOL_CHOICES, default='Freshman',)

    def __str__(self):
        return self.username + ' (' + str(self.userID) + ')'

'''

'''
    MEMBER_STATUS_CHOICES = (
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Diamond', 'Diamond'),
        ('Platinum', 'Platinum'),
        ('Admin', 'Admin'),
        ('SUPER Admin', 'SUPER Admin'),
    )
    member_status = models.CharField(max_length=15, choices=MEMBER_STATUS_CHOICES, default='Bronze',)
'''




class MessagesInAChat(models.Model):
    class Meta:
        verbose_name_plural = "Messages In A Chat"
    messageID   = models.AutoField(primary_key=True)
    chatID      = models.ForeignKey(
                    'ListofChats',
                     on_delete=models.PROTECT,
                )
    userID      = models.ForeignKey(
                    User,
                     on_delete=models.PROTECT,
                )
    message     = models.CharField(max_length = 100)
    dateTime    = models.DateTimeField(auto_now_add=True) #FIX TIMEZONE AMBIGUITY
    important   = models.BooleanField(default = False)
    flag        = models.BooleanField(default = False)
    rating      = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.chatID) + ' | ' + str(self.messageID) + ' : ' + self.message

class ListofChats(models.Model):
    class Meta:
        verbose_name_plural = "List of Chats"
    chatID              = models.AutoField(primary_key=True)
    className           = models.CharField(max_length = 30)
    professor           = models.CharField(max_length = 30)
    s_year              = models.CharField(max_length = 3)
    currently_active    = models.BooleanField(default = 0)
    university          = models.CharField(max_length = 45)

    def __str__(self):
        return self.className + ' (' + str(self.chatID) + ')'

class User_s_Chats(models.Model):
    class Meta:
        verbose_name_plural = "User's Chats"
    uscID           = models.AutoField(primary_key=True)
    chatID          = models.ForeignKey(
                        'ListofChats',
                         on_delete=models.PROTECT,
                    )
    owner           = models.ForeignKey(User,
                         on_delete=models.PROTECT,
                    )
    seen            = models.BooleanField(default = False)
    mutedStatus     = models.BooleanField(default = False)
    archived        = models.BooleanField(default = False)

    def __str__(self):
        return self.owner.email + ' | ' + self.chatID.className + ' | ' + self.chatID.professor + ' | ' + self.chatID.s_year + " | " + str(self.uscID)
    



