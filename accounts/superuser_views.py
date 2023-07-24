from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.db import IntegrityError
from .views import is_superuser, is_admin, is_staff




""" 

! CRUD admins as Superusers 

"""

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class SuperUserDashboardView(View):
    def get(self, request):
        User = get_user_model()
        admins = User.objects.filter(is_admin=True)
        return render(request, 'superuser/superuser_dashboard.html', {'admins': admins})
    

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class CreateAdminView(View):
    def get(self, request):
        return render(request, 'superuser/create_admin.html')

    def post(self, request):
        User = get_user_model()
        try:
            new_admin = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                is_admin=True
            )
            return redirect('superuser_dashboard')
        except IntegrityError:
            return render(request, 'create_admin.html', {
                'error': 'Username already taken.'
            })



@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class EditAdminView(View):
    def get(self, request, user_id):
        User = get_user_model()
        admin = get_object_or_404(User, pk=user_id)
        return render(request, 'superuser/edit_admin.html', {'admin': admin})

    def post(self, request, user_id):
        User = get_user_model()
        admin = get_object_or_404(User, pk=user_id)
        try:
            admin.username = request.POST['username']
            admin.save()
            return redirect('superuser_dashboard')
        except IntegrityError:
            return render(request, 'edit_admin.html', {
                'admin': admin,
                'error': 'Username already taken.'
            })

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser), name='dispatch')
class DeleteAdminView(View):
    def get(self, request, user_id):
        User = get_user_model()
        admin = get_object_or_404(User, pk=user_id)
        admin.delete()
        return redirect('superuser_dashboard')


