from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse("Hello")
    return render(request, "unijive.home_logged_out.html",{})
