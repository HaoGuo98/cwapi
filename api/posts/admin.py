from django.contrib import admin

# Register your models here.
# posts/admin.py

from . models import Teacher,Student,Module,Rank
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Rank)
