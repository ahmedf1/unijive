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

    def __str__(self):
        return self.username + ' (' + str(self.userID) + ')'


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
    chatID       = models.AutoField(primary_key=True)
    className    = models.CharField(max_length = 30)
    professor    = models.CharField(max_length = 30)
    s_year       = models.CharField(max_length = 3)

    def __str__(self):
        return self.className + ' (' + str(self.chatID) + ')'

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

    def __str__(self):
        return self.userID.username + ' | ' + self.chatID.className + ' ' + self.chatID.professor + ' ' + self.chatID.s_year
    



