from django.shortcuts import render
from django.views import View


# Create your views here.


"""
class HomeLoggedOut(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.home_logged_out.html", context)

class HomeLoggedIn(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.home_logged_in.html", context)

class HomeRegister(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.register.html", context)

class MyChats(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.my_chats.html", context)

class SearchChats(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.search_chats.html", context)

class ChatPage(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.chat_page.html", context)

class ChatsNearMe(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.chats_near_me.html", context)

class MyAccount(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "unijive.my_account.html", context)

"""