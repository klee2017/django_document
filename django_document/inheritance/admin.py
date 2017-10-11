from django.contrib import admin

from .models import Student, Teacher, School, Place, Restaurant, Champion

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Champion)
