from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Course URLs
    path("courses/", views.CourseListCreate.as_view(), name="course-create-views"),
    path("courses/<int:pk>/", views.CourseRetrieveUpdateDestroy.as_view(), name="course-update"),

    # Video URLs
    path("videos/", views.VideoListCreate.as_view(), name="video-create-views"),
    path("videos/<int:pk>/", views.VideoRetrieveUpdateDestroy.as_view(), name="video-update"),

    # Users URLs
    path("users/", views.UsersListCreate.as_view(), name="users-create-views"),
    path("users/<int:pk>/", views.UsersRetrieveUpdateDestroy.as_view(), name="users-update"),

    # FormUser URLs
    path("formusers/", views.FormUserListCreate.as_view(), name="formuser-create-views"),
    path("formusers/<int:pk>/", views.FormUserRetrieveUpdateDestroy.as_view(), name="formuser-update"),


# PDF Endpoints
    path("pdfs/", views.PDFListCreate.as_view(), name="pdf-create-list"),
    path("pdfs/<int:pk>/", views.PDFRetrieveUpdateDestroy.as_view(), name="pdf-detail")
    
]
