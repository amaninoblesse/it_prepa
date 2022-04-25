from pyexpat.errors import messages
from django.shortcuts import render,redirect
from it.models import NewUser
from it.forms import NewUserForm

def index(request):
    return render(request,'it/main/index.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("reussieeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            # messages.success(request, "Inscription réussie." )
            
            return redirect("../")
        # messages.error(request, "Inscription échouée. Information invalide.")
    form = NewUserForm()
    print("echoueeeeeeeeeeee")
    return render(request=request,template_name='it/main/register.html',context={"register_form":form})
    


# Create your views here.
