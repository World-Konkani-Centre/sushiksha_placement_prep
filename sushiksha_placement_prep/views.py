from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    messages.error(request, 'test')
    messages.info(request, "test")
    messages.success(request, 'test')
    messages.warning(request, 'test')
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'web/home.html')
