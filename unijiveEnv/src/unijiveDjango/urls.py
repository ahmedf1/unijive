"""unijiveDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView   

#from webpages.views import HomeLoggedIn,HomeLoggedOut,HomeRegister, MyChats, SearchChats,ChatPage
from webpages.views import ChatsListView, AccountDetailView, UserCreateView

#ChatsNearMe
#MyAccount  

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', UserCreateView.as_view(template_name = "unijive.home_logged_out.html")),
    url(r'^logged_in/$', TemplateView.as_view(template_name = "unijive.home_logged_in.html")),
    url(r'^register/$', TemplateView.as_view(template_name = "unijive.register.html")),

    url(r'^chat_page/$', TemplateView.as_view(template_name = "unijive.chat_page.html")),
    url(r'^my_chats/$', ChatsListView.as_view( template_name = 'unijive.my_chats.html') ),
    url(r'^my_chats/(?P<slug>\w+)/$', ChatsListView.as_view( template_name = 'unijive.my_chats.html') ),
   
    url(r'^search_chats/$', TemplateView.as_view(template_name = "unijive.search_chats.html")),
    url(r'^my_account/$', TemplateView.as_view(template_name = "unijive.my_account.html")),
    url(r'^my_account/(?P<pk>\w+)/$', AccountDetailView.as_view(template_name = "unijive.my_account.html")),
     #url(r'^my_chats/$', TemplateView.as_view(template_name = "unijive.my_chats.html")),
    # url(r'^chats_near_me/$', TemplateView.as_view(template_name = "unijive.chats_near_me.html")),
    


  
]




'''
    url(r'^$', HomeLoggedOut.as_view()),
    url(r'^logged_in/$', HomeLoggedIn.as_view()),
    url(r'^register/$', HomeRegister.as_view()),

    url(r'^chat_page/$', ChatPage.as_view()),
    url(r'^my_chats/$', MyChats.as_view()),
    url(r'^search_chats/$', SearchChats.as_view()),

   # url(r'^chats_near_me/$', ChatsNearMe.as_view()),
   # url(r'^my_account/$', MyAccount.as_view()),
'''


