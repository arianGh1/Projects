from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.db import IntegrityError






def is_superuser(user):
    return user.is_authenticated and user.is_superuser

def is_admin(user):
    return user.is_authenticated and user.is_admin

def is_staff(user):
    return user.is_authenticated and user.is_staff


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('superuser_dashboard')
            elif user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_staff:
                return redirect('staff_dashboard')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {
                'error': 'Invalid login credentials.'
            })






