from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse


def Student_details(request,pk):

    stu = Student.objects.get(id = pk) # get object querySet
    serializer = StudentSerializer(stu)  # convert complex data to python data
    json_data = JSONRenderer().render(serializer.data) #  convert python data to json data

    return HttpResponse(json_data, content_type="application/json")

    # return JsonResponse(serializer.data) It is shortcuts It remove to line of code json_data and return httpResponse



def Students_details(request):

    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type="application/json")
# Create your views here.
