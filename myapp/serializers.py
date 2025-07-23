from rest_framework import serializers
from .models import Course, Videos, Users, FormUser, PDF

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class FormUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormUser
        fields = '__all__'
        
        
class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'
