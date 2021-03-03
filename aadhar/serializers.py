from rest_framework import serializers
from .models import aadhar_model 

class aadhar_modelSerializer(serializers.Serializer):
    aadhar_number=serializers.CharField(help_text="enter aadhar number",max_length=13,default='')
    name=serializers.CharField(help_text="ENTER name",max_length=40,default='')
    age=serializers.CharField(help_text="enter age",max_length=3,default='')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return aadhar_model.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.aadhar_number = validated_data.get('aadhar_number', instance.aadhar_number)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
