from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views.cbv import StudentWorkPostAPIView, NewsPostAPIView, StudentWorkDiscussionAPIView, \
    NewsDiscussionAPIView, LessonAPIView

from core.views.fbv import lesson_detail

from core.views.viewsets import student_work_post_detail, news_post_detail

router = DefaultRouter()

router.register(r'studentWorkPosts', student_work_post_detail)
router.register(r'newsPosts', news_post_detail)

urlpatterns = [
    path('studentWorkPosts/', StudentWorkPostAPIView.as_view()),
    path('newsPosts/', NewsPostAPIView.as_view()),
    path('studentWorkDiscussions/', StudentWorkDiscussionAPIView.as_view()),
    path('newsDiscussions/', NewsDiscussionAPIView.as_view()),
    path('lessons/', LessonAPIView.as_view()),
    path('lessons/<int:pk>/', lesson_detail),
] + router.urls
