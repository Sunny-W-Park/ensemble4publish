from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import user
from django.http import HttpResponse

#Check Log-in
def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "Log-in required")
            return redirect(settings.LOGIN_URL)
        return function(request, *args, **kwargs)
    return wrap

#Check Auth
def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.level == '1' or reqeust.user.level == '0':
            return function(request, *args, **kwargs)
        messages.info(request, "No access")
        return redirect('/users/main/')
    return wrap

def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "This ID is already in use")
            return redirect('/users/main/')
        return function(request, *args, **kwargs)
    return wrap

