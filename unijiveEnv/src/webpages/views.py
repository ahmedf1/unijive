from django.conf import settings  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView


from .forms import UserCreateForm
from .models import ListofChats, User_s_Chats
 

User = settings.AUTH_USER_MODEL

# Create your views here.





class ChatsListView(LoginRequiredMixin, ListView):

    '''
    def get_queryset(self):
        slug = self.kwargs.get("slug")      #userID
        #int slugv2 = int(slug)
        if slug:
            queryset = User_s_Chats.objects.filter(
                Q(userID__exact = slug)
            )
        
        else:
            queryset = User_s_Chats.objects.none()
        return queryset
    '''

class AccountDetailView(LoginRequiredMixin, DetailView):
    
    '''
    queryset = User.objects.all()
 

    def get_object(self, *args, **kwargs):
        User = self.kwargs.get('pk')      #userID   4:32:00
        obj = get_object_or_404(User, userID=user_id)
        return obj
    '''


class LoggedInMainPageView(LoginRequiredMixin, TemplateView):
    x = "asdasd"    

class RegisterClassesView(LoginRequiredMixin, TemplateView):
    x = "asdasd"

class ChatPageView(LoginRequiredMixin, TemplateView):
    x = "asdasd"    


class SearchChatsView(LoginRequiredMixin, TemplateView):
    x = "asdasd"    


class DistractionsView(LoginRequiredMixin, TemplateView):
    x = "asdasd"    


class UserCreateView(CreateView):
    form_class         = UserCreateForm 
    success_url        =  "/register/"
    
