from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView


from .forms import UserCreateForm
from .models import ListofChats, User_s_Chats, User

# Create your views here.

class ChatsListView(ListView):
   

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

class AccountDetailView(DetailView):
    
    queryset = User.objects.all()
 

    def get_object(self, *args, **kwargs):
        user_id = self.kwargs.get('pk')      #userID
        obj = get_object_or_404(User, userID=user_id)
        return obj


class UserCreateView(CreateView):
    form_class         = UserCreateForm 
    success_url        =  "/register/"
    
