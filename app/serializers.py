from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Students
        # exclude = ['id', 'name'] Displays all the data excerpt id and name
        fields = '__all__' # Displays all the data
