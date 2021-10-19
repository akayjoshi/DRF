from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse



# Create your views here.
def stu_detail(request, id):
    stu = Student.objects.get(id=id) # complex data
    serializer = StudentSerializer(stu) # serialized data mean in python native dict in side .data attribute
    json_data = JSONRenderer().render(serializer.data) # convert data to JSON data
    return HttpResponse(json_data, content_type='application/json')

def stu_list(request):
    stu = Student.objects.all() # complex data
    serilizer = StudentSerializer(stu, many=True) # make list of serialized data
    # json_data = JSONRenderer().render(serilizer.data)
    return JsonResponse(serilizer.data, safe=False)