from django.shortcuts import render
from rest_framework import generics
from .models import Course, Videos, Users, FormUser, PDF
from .serializers import CourseSerializer, VideoSerializer, UsersSerializer, FormUserSerializer, PDFSerializer
from .permissions import AdminOrReadOnly  # ✅ Import your custom permission

# Course Views
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AdminOrReadOnly]  # ✅ Apply permission

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"
    permission_classes = [AdminOrReadOnly]  # ✅ Apply permission

# Video Views
class VideoListCreate(generics.ListCreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AdminOrReadOnly]

class VideoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    lookup_field = "pk"
    permission_classes = [AdminOrReadOnly]

# Users Views
class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AdminOrReadOnly]

class UsersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = "pk"
    permission_classes = [AdminOrReadOnly]

# FormUser Views
class FormUserListCreate(generics.ListCreateAPIView):
    queryset = FormUser.objects.all()
    serializer_class = FormUserSerializer
    # permission_classes = [AdminOrReadOnly]

class FormUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormUser.objects.all()
    serializer_class = FormUserSerializer
    lookup_field = "pk"
    permission_classes = [AdminOrReadOnly]

# PDF Views
class PDFListCreate(generics.ListCreateAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    permission_classes = [AdminOrReadOnly]

class PDFRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    lookup_field = "pk"
    permission_classes = [AdminOrReadOnly]

# Default index view
def index(request):
    return render(request, 'index.html')


