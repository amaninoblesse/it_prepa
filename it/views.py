from pyexpat.errors import messages
from django.shortcuts import render,redirect
from it.models import NewUser
from it.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this

def home(request):
    return render(request,'it/main/index.html')

def connexion(request):
    return render(request,'it/main/connexion.html')


def quiz(request):
    return render(request,'it/main/quiz.html')

def success(request):
    return render(request,'it/notification/success.html')

def fail(request):
    return render(request,'it/notification/fail.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("reussieeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            # messages.success(request, "Inscription réussie." )
            
            return redirect("../success")
        # messages.error(request, "Inscription échouée. Information invalide.")
    form = NewUserForm()
    print("echoueeeeeeeeeeee")
    return render(request=request,template_name='it/main/register.html',context={"form":form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("../quiz")
            else:
                messages.error(request,"Invalid username or password.")
                return redirect("../fail")
        else:
            messages.error(request,"Invalid username or password.")
            return redirect("../fail")
            print("erreuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuurrr")
    form = AuthenticationForm()
    return render(request=request, template_name="it/main/index.html", context={"login_form":form})   


# Create your views here.
