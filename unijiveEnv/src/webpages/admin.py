from django.contrib import admin

from .models import User, MessagesInAChat, ListofChats, User_s_Chats


# Register your models here.

class MessagesInAChatAdmin(admin.ModelAdmin):       #DISPLAYS TIME ON ADMIN SITE/ BUT DOES IT IN WRONG TIME ZONE
    readonly_fields = ('dateTime',)

admin.site.register(User)
admin.site.register(MessagesInAChat,MessagesInAChatAdmin)
admin.site.register(ListofChats)
admin.site.register(User_s_Chats)

