from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import permissions

from rest_framework import viewsets

from .import models
from .import serializers


class ListCreateCourse(generics.ListCreateAPIView):
    queryset         = models.Cource.objects.all()
    serializer_class = serializers.CourceSerializer

class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset         = models.Cource.objects.all()
    serializer_class = serializers.CourceSerializer

class ListCreateReview(generics.ListCreateAPIView):
    queryset         = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        cource = get_object_or_404(models.Cource,pk=self.kwargs.get('pk'))
        serializer.save(cource=cource)
    
class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset         = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('pk'),
            pk=self.kwargs.get('pk')
        )

#Routes
class ReviewViewSet(viewsets.ModelViewSet): 
    queryset         = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.user.is_superuser:
            return False
        else:
            if request.method == "DELETE":
                return False    






















