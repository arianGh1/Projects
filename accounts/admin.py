from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(CustomUser)
# admin.site.register(Person)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Applicant)