from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('students/', studentsList, name='home'),
    path('students/<int:pk>/', students),
]
urlpatterns = format_suffix_patterns(urlpatterns)