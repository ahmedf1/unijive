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
from django.contrib.auth.views import LoginView


from webpages.views import (ChatsListView, AccountDetailView, #UserCreateLoginView, 
                            LoggedInMainPageView, RegisterClassesView, ChatPageView,
                            SearchChatsView, DistractionsView, #login
                            )

#ChatsNearMe
#MyAccount  


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^login/$', login, name='login'),
    #url(r'^login/$', UserCreateLoginView.as_view(template_name = "unijive.home_logged_out.html"), name='login'),
    url(r'^login/$', LoginView.as_view(template_name = "unijive.home_logged_out.html",redirect_field_name = "/logged_in"), name='login'),
    #url(r'^login/$', UserCreateView.as_view(template_name = "unijive.home_logged_out.html")),
    url(r'^logged_in/$', LoggedInMainPageView.as_view(template_name = "unijive.home_logged_in.html"), name ='home'),
    url(r'^register/$', RegisterClassesView.as_view(template_name = "unijive.register.html"), name='addClasses'),

    url(r'^chat_page/$', ChatPageView.as_view(template_name = "unijive.chat_page.html")), # need customizable name
    url(r'^my_chats/$', ChatsListView.as_view( template_name = 'unijive.my_chats.html'),name="myChats"),
    #url(r'^my_chats/(?P<slug>\w+)/$', ChatsListView.as_view( template_name = 'unijive.my_chats.html') ),
   
    url(r'^search_chats/$', SearchChatsView.as_view(template_name = "unijive.search_chats.html"), name="searchChats"),
    url(r'^my_account/$', AccountDetailView.as_view(template_name = "unijive.my_account.html"), name='myAccount'),
    #url(r'^my_account/(?P<pk>\w+)/$', AccountDetailView.as_view(template_name = "unijive.my_account.html")),
     #url(r'^my_chats/$', TemplateView.as_view(template_name = "unijive.my_chats.html")),
    url(r'^distractions/$', DistractionsView.as_view(template_name = "unijive.distractions.html"), name="distractions"),
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


