from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .bot import Run
import threading

@login_required(login_url='/')
def index(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    return render(request, 'vipertbot/bot/index.html')


@login_required(login_url='/')
def start(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    botThread = threading.Thread(target=bot)
    botThread.daemon = True
    botThread.start()

    return render(request, 'vipertbot/bot/index.html')

@login_required(login_url='/')
def stop(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    return render(request, 'vipertbot/bot/index.html')

###############
### THREADS ###

# Main Bot Thread
def bot():
    Run.Main()