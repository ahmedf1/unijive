from django.conf import settings  
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.shortcuts import render, get_object_or_404, render_to_response, redirect, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView


from .forms import UserProfileCreateForm #UserCreateForm, UserInLineFormset
from .models import ListofChats, User_s_Chats
from accounts.models import User, UserProfile

#User = settings.AUTH_USER_MODEL

# Create your views here.

class ChatsListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = User_s_Chats.objects.filter(owner = self.request.user)
        return queryset


class AccountDetailView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        queryset = User_s_Chats.objects.filter(owner = self.request.user)
        return queryset

'''
    def get_object(self, *args, **kwargs):
        curr_User = self.request.user      #userID   4:32:00
        obj = get_object_or_404(User, email = curr_User.email)
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
    
    form_class         = UserProfileCreateForm 
    success_url        =  "/register/"
    '''
    template_name       = "unijive.home_logged_out.html"
    model               = User
    form_class          = UserCreateForm
    success_url         =  "/register/"

    #On successful form submission
    def get_success_url(self):
        return reverse("User Created")
    
    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save() # saves User and UserProfile
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(UserCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = UserCreateForm(self.request.POST)
            ctx['inlines'] = UserInLineFormset(self.request.POST)
        else:
            ctx['form'] = User()
            ctx['inlines'] = UserInLineFormset()
        return ctx
'''