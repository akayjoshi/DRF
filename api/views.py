from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
    if request.method == 'POST':
        json_data = request.body # request ki body json data hogi
        stream = io.BytesIO(json_data)  # convert json data to byte stream
        parsed_data = JSONParser().parse(stream) # parse stream to python native data type
        serializer = StudentSerializer(data = parsed_data) # deserialize python native data to complex datatype
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
        

