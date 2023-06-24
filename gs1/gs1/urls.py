
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentInfo/<int:pk>',views.Student_details, name="student_details"),
    path('studentInfo/',views.Students_details, name="students_details"),
]
