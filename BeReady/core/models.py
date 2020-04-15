from django.db import models
from authAB_.models import User


class AbstractPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='post_files', blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class StudentWorkPost(AbstractPost):
    class Meta:
        abstract = True
        verbose_name = 'StudentWorkPost'
        verbose_name_plural = 'StudentWorkPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class NewsPost(AbstractPost):
    class Meta:
        abstract = True
        verbose_name = 'NewsPost'
        verbose_name_plural = 'NewsPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class DiscussionAbstract(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'

    def __str__(self):
        return '{}: {}, {}'.format(self.comment, self.date, self.owner)


class StudentWorkDiscussion(DiscussionAbstract):
    post = models.ForeignKey(StudentWorkPost, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'StudentWorkDiscussion'
        verbose_name_plural = 'StudentWorkDiscussions'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.comment, self.date, self.owner, self.post)


class NewsDiscussion(DiscussionAbstract):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'NewsDiscussion'
        verbose_name_plural = 'NewsDiscussions'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.comment, self.date, self.owner, self.post)


class Class(models.Model):
    name = models.CharField(max_length=200)
    classCode = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')

    class Meta:
        abstract = True
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.name, self.subject, self.classCode, self.owner, self.students)


class Lesson(Class):
    faculty = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return '{}: {}, {}, {}, {}, {}'.format(self.name, self.subject, self.classCode, self.owner, self.students, self.faculty)
