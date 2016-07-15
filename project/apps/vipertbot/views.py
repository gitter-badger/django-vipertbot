from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated():
        return redirect('dashboard')

    return render(request, 'vipertbot/welcome.html')

@login_required(login_url='/')
def dashboard(request):
    #return render(request, 'vipertbot/dashboard.html')
    return render(request, 'smartadmin/index.html')

# @login_required(login_url='/')
# def admin(request):
#     if request.user.is_staff:
#         return redirect('/admin')
#
#     return redirect('#')

def logout(request):
    auth_logout(request)
    return redirect('/')