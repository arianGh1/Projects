from django.db import models
from django.contrib.auth.models import AbstractUser

""" 
Superuser registers -> admins -> staff

"""


# Create your models here.
class CustomUser(AbstractUser):
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)




class Person(models.Model):
    # Personal information
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    class Meta:
        abstract = True


class Applicant(Person):
    # Uploaded resume/CV
    resume = models.FileField(upload_to='resumes', blank=True, null=True)


class Parent(Person):
    username = models.CharField(max_length=120, blank=True, null=False)
    password = models.CharField(max_length=120, blank=True, null=False)


class Child(Person):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    fees_paid = models.DecimalField(max_digits=10, decimal_places=3)
    fees_left = models.DecimalField(max_digits=10, decimal_places=3)
    fee_due_date = models.DateField(blank=True, null=True)
    last_paid_date = models.DateField(blank=True, null=True)




