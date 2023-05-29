from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html',
                  {'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('flights')
            except IntegrityError:
                return render(request, 'signupaccount.html',
                          {'form':UserCreateForm,
                           'error':'Username already exists. Please choose a new username'})
        else:
            return render(request, 'signupaccount.html',
                      {'form':UserCreationForm,
                       'error':'Passwords did not match'})
        

def logoutaccount(request):
    logout(request)
    return redirect('flights')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',
                  {'form':AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html',
                      {'form':AuthenticationForm,
                       'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('flights')
