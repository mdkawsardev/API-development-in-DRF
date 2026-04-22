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
def studentsList(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
def students(request, pk):
    try:
        specific_obj = Students.objects.get(id=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(specific_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(specific_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        specific_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)