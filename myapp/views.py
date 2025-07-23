from django.shortcuts import render
from rest_framework import generics
from .models import Course, Videos, Users, FormUser, PDF
from .serializers import CourseSerializer, VideoSerializer, UsersSerializer, FormUserSerializer,PDFSerializer

# Course Views
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"

# Video Views
class VideoListCreate(generics.ListCreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer

class VideoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    lookup_field = "pk"

# Users Views
class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = "pk"

# FormUser Views
class FormUserListCreate(generics.ListCreateAPIView):
    queryset = FormUser.objects.all()
    serializer_class = FormUserSerializer

class FormUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormUser.objects.all()
    serializer_class = FormUserSerializer
    lookup_field = "pk"
    
    
# PDF Views
class PDFListCreate(generics.ListCreateAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class PDFRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    lookup_field = "pk"

# Default index view
def index(request):
    return render(request, 'index.html')

