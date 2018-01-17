from django.contrib import admin

from .models import User, MessagesInAChat, ListofChats, User_s_Chats


# Register your models here.

admin.site.register(User)
admin.site.register(MessagesInAChat)
admin.site.register(ListofChats)
admin.site.register(User_s_Chats)

