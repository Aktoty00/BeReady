from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student, Teacher, StudentProfile, TeacherProfile


@receiver(post_save, sender=Teacher)
def teacher_profile_create(sender, instance, created, **kwargs):
    if created:
        TeacherProfile.objects.create(user=instance)


@receiver(post_save, sender=Student)
def student_profile_create(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)


