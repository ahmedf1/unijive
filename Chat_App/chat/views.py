from django.shortcuts import render
from django.views.generic import ListView
from .models import Room


class ChatRoom(ListView):
    context_object_name = 'chat_list'
    queryset = Room.objects.order_by("title")
    template_name = "chat_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



