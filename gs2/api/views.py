from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def StudentCreate(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)

        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print("hellop")
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ="application/json")