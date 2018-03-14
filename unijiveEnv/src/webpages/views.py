from django.conf                import settings  
from django.contrib.auth        import authenticate, login, logout, get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models           import Q
from django.http                import HttpResponse, HttpResponseRedirect,HttpRequest
from django.shortcuts           import render, get_object_or_404, render_to_response, redirect, reverse
from django.views               import View
from django.views.generic       import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views  import LoginView
from django.contrib.auth        import logout, login
from django.contrib             import messages
from django.core                import serializers
import json
import ast

#from django.views.generic.edit.FormMixin import get_form_class

#from .forms import UserProfileCreateForm, UserCreateForm, UserInLineFormset
from .models                    import ListofChats, User_s_Chats
from accounts.models            import User, UserProfile, UserManager

def isEmailPresent(email):
    return User.objects.filter(email=email).exists()
    
def isUsernamePresent(username):
    return UserProfile.objects.filter(username=username).exists()

def isPasswordValid(password):
    if len(password) in range(8,15):
        return True
    else:
        return False



def userCreate(request):
    if request.method == 'POST':
        fName           = str(request.POST.get('fName', ''))
        lName           = str(request.POST.get('lName', ''))
        university      = str(request.POST.get('university', ''))
        email           = str(request.POST.get('email', ''))
        username        = str(request.POST.get('username', ''))
        password        = str(request.POST.get('password', ''))
        confirmPassword = str(request.POST.get('confirmPassword', ''))
        '''
        print(fName)
        print(lName)
        print(email)
        print(username)
        '''
        # now for some form validation
        #first check database for existing userid and email since these need to be unique to each user

                    
        if isEmailPresent(email):
            messages.error(request,"This email is already registered to an existing user!")
            

        if isUsernamePresent(username):
            messages.error(request,"This username already belongs to an existing user!")
            


        if not isEmailPresent(email) and not isUsernamePresent(username):
            # this is checking to make sure first name and last name only include letters
            isFNameValid        = fName.isalpha()  
            isLNameValid        = lName.isalpha()
            isUserNameValid     = True if username.isalnum() and len(username) in range(5,12)   else False
            isNyuEmail          = True if "@nyu.edu" in email                                   else False   #Currently only serves NYU
            passwordsMatch      = True if password == confirmPassword                           else False

            if not isFNameValid: messages.error(request,"The First Name Entered is not Valid!")
            
            if not isLNameValid: messages.error(request,"The Last Name Entered is not Valid!")

            if not isUserNameValid: messages.error(request,"Username should only include letters and numbers and be between 5 and 12 characters long!")
            
            if not isNyuEmail: messages.error(request, "Please use the email associated with your university!")
            
            if not passwordsMatch: messages.error(request, "Please make sure that the passwords match!")
            
            elif passwordsMatch: #already confirmed that they match, now checking if it's valid
                isValid = isPasswordValid(password)
                if not isValid:
                    messages.error(request, "Passwords should be between 8 and 15 characters!")

            if isFNameValid and isLNameValid and isUserNameValid and isNyuEmail and passwordsMatch and isPasswordValid(password):
                #create instance of user and save to db
                print("here")
                newUser = User(email=email)
                newUser.set_password(password)
                newUser.save()

                newUserProfile = UserProfile()
                newUserProfile.user = newUser
                newUserProfile.firstName = fName
                newUserProfile.lastName = lName
                newUserProfile.username = username
                newUserProfile.university = university
                newUserProfile.save()
                

                user = authenticate(username = email, password = password)
                login(request, user)
                return HttpResponseRedirect('/search_chats/')
                
                


            

def mute_chat(request):       
    if request.method == 'GET':
        userChatID = request.GET['userChatID']
        mutedChat = User_s_Chats.objects.get(pk=userChatID)
        mutedChat.mutedStatus = not mutedChat.mutedStatus
        mutedChat.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("FAILED!")


def leave_chat(request):       
    if request.method == 'GET':
        userChatID = request.GET['userChatID']
        archivedChat = User_s_Chats.objects.get(pk=userChatID)
        archivedChat.archived = True
        archivedChat.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("FAILED!")

        

def logout_view(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.


def unopenedChatCounter(request):
        count = 0
        usersChats = User_s_Chats.objects.filter(owner = request.user)
        for usersChat in usersChats:
            if (usersChat.seen == False):
                count+=1
        return count
        

def professorsSubQuery(request):
    if request.method == "GET":
        classSelected = request.GET['class']
        classToFilterOn = ListofChats.objects.filter(className=classSelected)       #all classes that have that name
        data = serializers.serialize("json", classToFilterOn)
        data = data.replace('true','True')
        data = data.replace('false','False')
        data = ast.literal_eval(data)
        returnDict = {}
        dictKey = 0
        for i in data:
            x = i['fields']['professor']
            returnDict[dictKey] = x
            dictKey += 1
        
        json_object = json.dumps(returnDict)
        return HttpResponse(json_object)
        

'''
[{"model": "webpages.listofchats", "pk": 12, "fields": {
    "subject": "CS", "className": "Software Engineering", "professor": "Strauss, Fred", "s_year": "S18", "currently_active": True, "university": "NYU"}}, 
{"model": "webpages.listofchats", "pk": 13, "fields": {"subject": "cs", "className": "Software Engineering", "professor": "Shadman Ahmed", "s_year": "s18", "currently_active": True, "university": "NYU"}}]
'''


class ChatsListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = User_s_Chats.objects.filter(owner = self.request.user)
        return queryset

class SearchChatsView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = ListofChats.objects.filter(university = self.request.user.userprofile.university).values('className').distinct()
        return queryset

    
   

class AccountDetailView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = User_s_Chats.objects.filter(owner = self.request.user)
        return queryset

class LoggedInMainPageView(LoginRequiredMixin, TemplateView):
    x = "asdasd"  
      
class RegisterClassesView(LoginRequiredMixin, TemplateView):
    x = "asdasd"

class DistractionsView(LoginRequiredMixin, TemplateView):
    x = "asdasd"    

class ChatPageView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = User_s_Chats.objects.filter(owner = self.request.user)
        return queryset   




#Create your views here.
'''
from django.contrib.auth import authenticate, login
def login(request):
    email = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        redirect()
    #else:
        # Return an 'invalid login' error message.
        #..
    return render(request, "unijive.home_logged_out.html")
'''

'''
from django.contrib.auth import authenticate, login
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    # Redirect to a success page.


from django.contrib.auth import update_session_auth_hash
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...

'''


'''
class UserCreateLoginView(CreateView):
    form_class          = UserCreateForm
    success_url         = "/register/"
    
''' 
'''
class UserCreateView(CreateView):
  
    form_class         = UserProfileCreateForm 
    success_url        =  "/register/"
    
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