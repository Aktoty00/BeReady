from django.urls import path

from .views import StudentWorkPostAPIView, NewsPostAPIView, DiscussionWithReplyAPIView, \
    DiscussionWithoutReplyAPIView, NewsDiscussionAPIView, LessonAPIView

urlpatterns = [
    path('studentWorkPosts/', StudentWorkPostAPIView.as_view()),
    path('newsPosts/', NewsPostAPIView.as_view()),
    path('discussionWithReplies/', DiscussionWithReplyAPIView.as_view()),
    path('discussionWithoutReplies/', DiscussionWithoutReplyAPIView.as_view()),
    path('newsDiscussions/', NewsDiscussionAPIView.as_view()),
    path('lessons/', LessonAPIView.as_view()),
]