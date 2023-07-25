
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login
from django.views import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from .models import Parent
# from django.conf import settings
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password





import random
import string




from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator



def is_staff(user):
    return user.is_staff


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_staff), name='dispatch')
class StaffDashboardView(View):
    def get(self, request):
        parents = Parent.objects.all()
        return render(request, 'staff/staff_dashboard.html', {'parents': parents})


# @method_decorator(login_required, name='dispatch')
# @method_decorator(user_passes_test(is_staff), name='dispatch')
# class RemindParentView(View):
#     def post(self, request, parent_id):
#         parent = get_object_or_404(Parent, pk=parent_id)
#         send_telegram_message(parent.phone_number, "Payment due reminder message")  # Adjust this as per your Telegram function
#         return redirect('staff_dashboard')


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_staff), name='dispatch')
class DeleteParentView(View):
    def post(self, request, parent_id):
        parent = get_object_or_404(Parent, pk=parent_id)
        parent.delete()
        redirect('staff/staff_dashboard')


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_staff), name='dispatch')
class UpdateParentView(View):
    def get(self, request, parent_id):
        parent = get_object_or_404(Parent, pk=parent_id)
        return render(request, 'staff/update_parent.html', {'parent': parent})

    def post(self, request, parent_id):
        parent = get_object_or_404(Parent, pk=parent_id)
        parent.name = request.POST['name']
        parent.surname = request.POST['surname']
        parent.phone_number = request.POST['phone_number']
        parent.email = request.POST['email']
        parent.save()
        return redirect('staff_dashboard')



@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_staff), name='dispatch')
class RegisterParentView(View):

    def generate_username(self, name, surname):
    # Generate a random number
        random_number = ''.join(random.choice(string.digits) for _ in range(4))
        
        # Concatenate the name, surname, and random number to create a username
        username = f'{name}_{surname}_{random_number}'

        # Ensure username is unique
        while Parent.objects.filter(username=username).exists():
            random_number = ''.join(random.choice(string.digits) for _ in range(4))
            username = f'{name}_{surname}_{random_number}'

        return username

    
    def generate_password(self):
        password = ''.join(random.choice(string.ascii_letters) for i in range(9))
        return password

       
    def get(self, request):
        return render(request,'staff/register_parent.html')
    
    def post(self, request):
        try:
            password = self.generate_password()
            hashed_password = make_password(password)
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            username = self.generate_username(name, surname)
            new_parent = Parent.objects.create(
                        name = name,
                        surname = surname,
                        phone_number = request.POST.get('phone_number'),
                        username = username,
                        password = hashed_password,
                        email = request.POST.get('email')
            )

            # Validate Email
            try:
                validate_email(new_parent.email)
            except ValidationError as e:
                return render(request, 'staff/register_parent.html', {'error': str(e)})
            
            # send_mail(
            #     'Welcome to Our System',
            #     'Here is your username: {username} and password: {password}'.format(
            #         username=new_parent.username, 
            #         password=new_parent.password
            #     ),
            #     'thebekhruz@gmail.com',
            #     [new_parent.email],
            #     fail_silently=False,
            # )

            return redirect('staff_dashboard')
        except IntegrityError:
            return render(request, 'staff/register_parent.html', {'error': 'Username already taken.'})





# @method_decorator(login_required, name='dispatch')
# @method_decorator(user_passes_test(is_staff), name='dispatch')
# class ListParentsView(View):
#     def get(self, request):
#         parents = Parent.objects.all()
#         return render(request, 'list_parents.html', {'parents': parents})
    




class ParentViewList(View):
    pass

class ApplicantsList(View):
    pass

class ResumeView(View):
    pass
