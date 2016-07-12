from django.shortcuts import render
from .bot import Run
import subprocess, sys, thread, threading

def run(request):
    botThread = threading.Thread(target=bot)
    botThread.daemon = True
    botThread.start()

    return render(request, 'vipertbot/bot/index.html')


def bot():
    Run.Main()