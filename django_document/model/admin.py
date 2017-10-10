from django.contrib import admin

from .models import Manufacturer, User, Car

admin.register.site(Car)
admin.register.site(Manufacturer)
admin.register.site(User)
