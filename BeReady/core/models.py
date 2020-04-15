from django.db import models

# from BeReady.BeReady.authAB_.models import Teacher, Student
from authAB_.models import Teacher, Student


class Discussion(models.Model):
    OWNER = (
        ('teacher', Teacher),
        ('student', Student)
    )
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(choices=OWNER, max_length=200)

    class Meta:
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'

    def __str__(self):
        return '{}: {}'.format(self.comment, self.date)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers')
    discussion = models.ForeignKey(Discussion, models.SET_NULL, blank=True, null=True, related_name='discussions')
    file = models.FileField(upload_to='post_files', blank=True, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{}: {}, {}'.format(self.title, self.discussion, self.discussion)


class Class(models.Model):
    name = models.CharField(max_length=200)
    classCode = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    post = models.ForeignKey(Post, models.SET_NULL, blank=True, null=True, related_name='posts')

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return '{}: {}'.format(self.name, self.subject)


