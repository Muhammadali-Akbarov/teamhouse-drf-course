from django.urls import path
from .views import (
    ListCreateCourse,
    ListCreateReview,
    RetrieveUpdateDestroyCourse
)

urlpatterns = [

    path('',ListCreateCourse.as_view(),name='course_lists'),
    path('<str:pk>/',RetrieveUpdateDestroyCourse.as_view(),name='course_detail'),
    path('<str:pk>/reviews/',ListCreateReview.as_view(),name='review_detail'),

]
