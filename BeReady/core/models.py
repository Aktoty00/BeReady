from django.db import models
from authAB_.models import User


class AbstractPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        verbose_name = 'AbstractPost'
        verbose_name_plural = 'AbstractPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class StudentWorkPost(AbstractPost):
    file = models.FileField(upload_to='student_work_posts', blank=True, null=True)

    class Meta:
        verbose_name = 'StudentWorkPost'
        verbose_name_plural = 'StudentWorkPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class NewsPost(AbstractPost):
    file = models.FileField(upload_to='news_posts', blank=True, null=True)

    class Meta:
        verbose_name = 'NewsPost'
        verbose_name_plural = 'NewsPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class AbstractDiscussion(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        verbose_name = 'AbstractDiscussion'
        verbose_name_plural = 'AbstractDiscussions'

    def __str__(self):
        return '{}: {}'.format(self.comment, self.date)


class AbstractPostDiscussion(AbstractDiscussion):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='AbstractPostDiscussionOwner')

    class Meta:
        abstract = True
        verbose_name = 'AbstractPostDiscussion'
        verbose_name_plural = 'AbstractPostDiscussions'

    def __str__(self):
        return '{}: {}, {}'.format(self.comment, self.date, self.owner)


class AbstractStudentWorkDiscussion(AbstractPostDiscussion):
    post = models.ForeignKey(StudentWorkPost, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        verbose_name = 'AbstractStudentWorkDiscussion'
        verbose_name_plural = 'AbstractStudentWorkDiscussions'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.comment, self.date, self.owner, self.post)


class StudentWorkDiscussionWithReply(AbstractStudentWorkDiscussion):
    sendTo = models.ForeignKey(User, related_name='from_owner_send_to', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='StudentWorkDiscussionWithReplyOwner')

    class Meta:
        verbose_name = 'StudentWorkDiscussionWithReply'
        verbose_name_plural = 'StudentWorkDiscussionWithReplies'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.comment, self.date, self.sendTo, self.owner, self.post)


class StudentWorkDiscussionWithoutReply(AbstractStudentWorkDiscussion):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='StudentWorkDiscussionWithoutReplyOwner')

    class Meta:
        verbose_name = 'StudentWorkDiscussionWithoutReply'
        verbose_name_plural = 'StudentWorkDiscussionWithoutReplies'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.comment, self.date, self.owner, self.post)


class NewsDiscussion(AbstractPostDiscussion):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'NewsDiscussion'
        verbose_name_plural = 'NewsDiscussions'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.comment, self.date, self.owner, self.post)


class Class(models.Model):
    name = models.CharField(max_length=200)
    classCode = models.CharField(max_length=200)

    class Meta:
        abstract = True
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return '{}: {}'.format(self.name, self.classCode)


class Lesson(Class):
    subject = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.name, self.subject, self.classCode, self.owner, self.students)
