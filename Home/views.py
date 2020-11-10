from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, PermissionDenied
from django.contrib import messages
from aqg.decorators import student_only, role_required
from django.contrib.auth.models import User


# Create your views here.

def handleSHome(request):
    return render(request, 'home/index.html')

def indexView(request):
    return render(request, 'home/index.html')

def csView(request):
    return render(request, 'comingsoon.html')

def handleSLogin(request):
    if request.method == 'POST':
        # get the post parameters
        print('i am here ')
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']


        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged In')
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return redirect('indexView')
        else:
            messages.error(request, 'Invalid: try again')
            return redirect('indexView')

    return render(request, 'login/login.html')

@login_required
# role_required(allowed_roles=['Teacher'])
@student_only
def handleSLogout(request):
    logout(request)
    messages.success(request, 'Success: Log Out')
    return redirect('indexView')
