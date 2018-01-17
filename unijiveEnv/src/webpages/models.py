from django.db import models

# Create your models here.


class User(models.Model):
    class Meta:
        verbose_name_plural = "Users"
    userID      = models.AutoField(primary_key=True)
    username    = models.CharField(max_length = 30)
    university  = models.CharField(max_length = 30)
    firstName   = models.CharField(max_length = 30)
    lastName    = models.CharField(max_length = 30)
    password    = models.CharField(max_length = 20)  #ADD VALIDATORS


class MessagesInAChat(models.Model):
    class Meta:
        verbose_name_plural = "Messages In A Chat"
    messageID   = models.AutoField(primary_key=True)
    chatID      = models.ForeignKey(
                    'ListofChats',
                     on_delete=models.PROTECT,
                )
    userID      = models.ForeignKey(
                    'User',
                     on_delete=models.PROTECT,
                )
    message     = models.CharField(max_length = 30)
    dateTime    = models.DateTimeField(auto_now_add=True)
    important   = models.BooleanField(default = False)
    flag        = models.BooleanField(default = False)
    rating      = models.IntegerField(default = 0)

class ListofChats(models.Model):
    class Meta:
        verbose_name_plural = "List of Chats"
    chatID       = models.AutoField(primary_key=True)
    className    = models.CharField(max_length = 30)
    professor    = models.CharField(max_length = 30)
    s_year       = models.CharField(max_length = 3)

class User_s_Chats(models.Model):
    class Meta:
        verbose_name_plural = "User's Chats"
    uscID          = models.AutoField(primary_key=True)
    chatID         = models.ForeignKey(
                        'ListofChats',
                         on_delete=models.PROTECT,
                    )
    userID         = models.ForeignKey(
                        'User',
                         on_delete=models.PROTECT,
                    )
    status         = models.BooleanField(default = False)
    mutedStatus    = models.BooleanField(default = False)
    username       = models.CharField(max_length = 30)



