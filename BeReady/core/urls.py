from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views.cbv import StudentWorkPostAPIView, NewsPostAPIView, \
    NewsDiscussionAPIView, LessonAPIView

from core.views.fbv import lesson_detail

from core.views.viewsets import StudentWorkPostDetail, NewsPostDetail, \
    SWDiscussionsViewSet, NewsDiscussionsViewSet

router = DefaultRouter()

router.register(r'studentWorkPosts', StudentWorkPostDetail)
router.register(r'newsPosts', NewsPostDetail)
router.register(r'studentWorkDiscussions', SWDiscussionsViewSet)
router.register(r'newsDiscussions', NewsDiscussionsViewSet)

urlpatterns = [
    # path('studentWorkPosts/', StudentWorkPostAPIView.as_view()),
    path('newsPosts/', NewsPostAPIView.as_view()),
    path('lessons/', LessonAPIView.as_view()),
    path('lessons/<int:pk>/', lesson_detail),
] + router.urls
