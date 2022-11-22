from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from home.models import Destination

# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is Homepage")

def login(request):
    if request.method =="POST":
        email_login=request.POST['email_login']
        psw_login=request.POST['psw_login']
        User = authenticate(request,email_login=email_login,psw_login=psw_login)
        if User is not None:
            login(request,User)
            print('Success')
            #messages.error(request,"User does not exists")
            #messages.success(request,"Successfully login")
            return redirect("login")
        else:
            #messages.success(request,"Successfully login")
            #messages.error(request,"User does not exists")
            print('User does not exists')
            return redirect("/")
    else:
        return render(request,"login.html")

def login_out(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect("/")

def incidents(request):
    if request.method == 'POST':
        print('Hi')
        initial_reporting = request.POST['initial_reporting']
        incident_description = request.POST['incident_description']
        birthday = request.POST['birthday']
        incident_location = request.POST['incident_location']
        initial_severity = request.POST['initial_severity']
        suspected_cause = request.POST['suspected_cause']
        immediate_actions_taken = request.POST['immediate_actions_taken']
        gridRadios = request.POST["gridRadios"]
        print(initial_reporting)
        print(incident_description)
        print(birthday)
        print(incident_location)
        print(initial_severity)
        print(immediate_actions_taken)
        print(suspected_cause)
        print(gridRadios)
        b = Destination(location=initial_reporting,incident_desc=incident_description,datetime=birthday,incident_loc=incident_location,initial_severity=initial_severity,suspected_cause=suspected_cause,immediate_actions_taken=immediate_actions_taken)#sub_incident_types=gridRadios
        b.save()
        return redirect("/")
    else:
        return render(request,"incident.html")
       


def register(request):
    if request.method == "POST":
        email=request.POST['email']
        psw=request.POST['psw']
        psw_repeat=request.POST['psw_repeat']
        if len(email) < 10:
            messages.error(request,"Username must be greater than 10 Characters")
            return redirect("register")
        if psw!=psw_repeat:
            messages.error(request,"Password Do not Match")
            return redirect("register")
        myuser = User.objects.create_user(email, psw, psw_repeat)
        myuser.save()
        messages.success(request,"Your account has been succesfully created !")
        return redirect("register")
    else:
        return render(request,"register.html")