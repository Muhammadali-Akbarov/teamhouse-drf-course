from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Cource,

)
from .serializers import (
    CourceSerializer,

)
from rest_framework import status

class ListCreateCourse(APIView):

    def get(self,request,format=None):
        courses = Cource.objects.all()
        serializer = CourceSerializer(courses,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args, **kwargs):
        serializer = serializers.CourceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



