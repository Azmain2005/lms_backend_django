from django.contrib import admin
from .models import Course, Videos, Users, FormUser, PDF

# Register your models here.
admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(Users)
admin.site.register(FormUser)
admin.site.register(PDF)
