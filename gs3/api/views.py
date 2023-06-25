from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from. models import Student
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def StudentApi(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata =  JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata =  JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            data = {'msg' :'data created'}
            json_data = JSONRenderer().render(data)
            return HttpResponse(json_data, content_type='application/api')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/api')
    
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata =  JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data = pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            data = {'msg' :'data updated'}
            json_data = JSONRenderer().render(data)
            return HttpResponse(json_data, content_type='application/api')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/api')
    
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata =  JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        data = {'msg' :'data Deleted'}
        
        json_data = JSONRenderer().render(data)
        return HttpResponse(json_data, content_type='application/api')
        

            

