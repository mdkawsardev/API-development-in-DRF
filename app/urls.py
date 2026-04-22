from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)