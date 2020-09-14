from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Recommendations
from .serializers import RecSysSerializer
from .recommendations import recommendation
from django.views.decorators.csrf import csrf_exempt
import os
import json

@csrf_exempt
def RecSys_list(request):


    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecSysSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        movie_name = data["movie"]
        df = recommendation(movie_name)
        data2 = df[['title']].head(10)
        # Work on getting output in proper format
        data2 = data2.to_dict()
        json_string = json.dumps(data2)


        return JsonResponse(json_string, safe=False)
