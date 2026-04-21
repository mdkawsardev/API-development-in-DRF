from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer
from rest_framework import status

def index(request):
    return render(request, 'index.html')

# @api_view(['GET'])
# def students(request):
#     details = {
#         'Name': 'Kawsar',
#         'Age': 23,
#         'Nationality': 'Bangladeshi'
#     }
#     return Response(details)

@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        obj = Students.objects.all()
        serializer = StudentSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)