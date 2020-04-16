from django.urls import path

from .views import StudentWorkPostAPIView, NewsPostAPIView, StudentWorkDiscussionAPIView, \
    NewsDiscussionAPIView, LessonAPIView

urlpatterns = [
    path('studentWorkPosts/', StudentWorkPostAPIView.as_view()),
    path('newsPosts/', NewsPostAPIView.as_view()),
    path('studentWorkDiscussions/', StudentWorkDiscussionAPIView.as_view()),
    path('newsDiscussions/', NewsDiscussionAPIView.as_view()),
    path('lessons/', LessonAPIView.as_view()),
]
