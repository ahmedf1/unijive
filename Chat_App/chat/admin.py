from django.contrib import admin
from . import models

# Register your models here.
#TODO: Modify this for Unijive models
admin.site.register(
    models.Room,
    # todo: What is the purpose of these two?
    list_display=["title", 'staff_only'],
    list_display_links=["title"]
)