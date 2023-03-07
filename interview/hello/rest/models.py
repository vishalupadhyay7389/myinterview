from django.db import models
from rest_framework import serializers

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'