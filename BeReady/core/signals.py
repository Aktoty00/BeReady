from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StudentWorkPost, LastNotificationStudentWorkPost, \
    StudentWorkDiscussion, LastNotificationStudentWorkDiscussions


@receiver(post_save, sender=StudentWorkPost)
def notification_student_work_posts(sender, instance, created, **kwargs):
    if created:
        LastNotificationStudentWorkPost.objects.create(last_posts=instance)


@receiver(post_save, sender=StudentWorkDiscussion)
def notification_student_work_posts_discussion(sender, instance, created, **kwargs):
    if created:
        LastNotificationStudentWorkDiscussions.objects.create(last_discussions=instance)
