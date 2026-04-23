from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_name']

class StudentSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = Students
        # exclude = ['id', 'name'] Displays all the data excerpt id and name
        fields = '__all__' # Displays all the data
        # depth = 1 # it displays all the data from rows including id, but serializer gives more control which I did above
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be above of 18')
        specialchars = "!@#$%^&*()-=<>?/:'\n"
        if any(a in specialchars for a in data['name']):
            raise serializers.ValidationError('Special characters are not allowed in name!')
        return data
