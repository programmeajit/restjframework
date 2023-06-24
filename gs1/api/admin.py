from django.contrib import admin

from .models import Student

#admin.site.register(Student)
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name","roll","city"]

