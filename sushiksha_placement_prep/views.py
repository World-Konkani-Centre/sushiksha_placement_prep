from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'web/home.html')


def handler404(request, exception):
    context = {
        'error_no': 404,
        'error_detail': 'Page Not Found'
    }
    return render(request, 'web/error.html', context)


def handler500(request):
    context = {
        'error_no': 500,
        'error_detail': 'Server Error'
    }
    return render(request, 'web/error.html', context)


def handler400(request, exception):
    context = {
        'error_no': 400,
        'error_detail': 'Bad Request'
    }
    return render(request, 'web/error.html', context)


def handler403(request, exception):
    context = {
        'error_no': 403,
        'error_detail': 'Permission Denied'
    }
    return render(request, 'web/error.html', context)
