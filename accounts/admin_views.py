from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from .views import is_superuser, is_admin, is_staff


""" 


! CRUD Stuff as Admins

"""

def is_admin(user):
    return user.is_admin

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class AdminDashboardView(View):
    def get(self, request):
        User = get_user_model()
        staff = User.objects.filter(is_staff=True)
        return render(request, 'admin/admin_dashboard.html', {'staff': staff})

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class CreateStaffView(View):
    def get(self, request):
        return render(request, 'admin/create_staff.html')

    def post(self, request):
        User = get_user_model()
        try:
            new_staff = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                is_staff=True
            )
            return redirect('admin_dashboard')
        except IntegrityError:
            return render(request, 'admin/create_staff.html', {'error': 'Username already taken.'})

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class EditStaffView(View):
    def get(self, request, user_id):
        User = get_user_model()
        staff = get_object_or_404(User, pk=user_id)
        return render(request, 'admin/edit_staff.html', {'staff': staff})

    def post(self, request, user_id):
        User = get_user_model()
        staff = get_object_or_404(User, pk=user_id)
        try:
            staff.username = request.POST['username']
            staff.save()
            return redirect('admin_dashboard')
        except IntegrityError:
            return render(request, 'edit_staff.html', {'error': 'Username already taken.', 'staff': staff})

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_admin), name='dispatch')
class DeleteStaffView(View):
    def get(self, request, user_id):
        User = get_user_model()
        staff = get_object_or_404(User, pk=user_id)
        staff.delete()
        return redirect('admin_dashboard')