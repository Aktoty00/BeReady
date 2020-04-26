from django.db import models
import datetime

from authAB_.models import Teacher, Student, MyUser


class DianaManager(models.Manager):
    def diana_objects(self):
        return self.filter(owner='Diana')


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
    subject = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    students = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='lessons')

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.name, self.subject, self.classCode, self.owner, self.students)


class AbstractPost(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        verbose_name = 'AbstractPost'
        verbose_name_plural = 'AbstractPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class StudentWorkPost(AbstractPost):
    file = models.FileField(upload_to='student_work_posts', blank=True, null=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='sw_posts')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='posts', default=5)

    class Meta:
        verbose_name = 'StudentWorkPost'
        verbose_name_plural = 'StudentWorkPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class NewsPost(AbstractPost):
    file = models.FileField(upload_to='news_posts', blank=True, null=True)
    objects = models.Manager()
    diana_objects = DianaManager()
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='news_posts')

    class Meta:
        verbose_name = 'NewsPost'
        verbose_name_plural = 'NewsPosts'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.title, self.description, self.date, self.owner, self.file)


class DiscussionManager(models.Manager):
    def today_discussion(self):
        return self.filter(date=datetime.date.today())


class AbstractDiscussion(models.Model):
    comment = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        verbose_name = 'AbstractDiscussion'
        verbose_name_plural = 'AbstractDiscussions'

    def __str__(self):
        return '{}: {}'.format(self.comment, self.date)


class AbstractPostDiscussion(AbstractDiscussion):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='abstractPostDiscussion')

    class Meta:
        abstract = True
        verbose_name = 'AbstractPostDiscussion'
        verbose_name_plural = 'AbstractPostDiscussions'

    def __str__(self):
        return '{}: {}, {}'.format(self.comment, self.date, self.owner)


class AbstractStudentWorkDiscussion(AbstractPostDiscussion):
    post = models.ForeignKey(StudentWorkPost, on_delete=models.CASCADE,  related_name='studentWorkDiscussion_post')

    class Meta:
        abstract = True
        verbose_name = 'AbstractStudentWorkDiscussion'
        verbose_name_plural = 'AbstractStudentWorkDiscussions'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.comment, self.date, self.owner, self.post)


class StudentWorkDiscussion(AbstractStudentWorkDiscussion):
    sendTo = models.ForeignKey(Teacher, related_name='from_owner_send_to', on_delete=models.CASCADE)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='studentWorkDiscussion_owner')
    objects = DiscussionManager()

    class Meta:
        verbose_name = 'StudentWorkDiscussion'
        verbose_name_plural = 'StudentWorkDiscussion'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.comment, self.date, self.sendTo, self.owner, self.post)


class NewsDiscussion(AbstractPostDiscussion):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='newsDiscussion_post')

    class Meta:
        verbose_name = 'NewsDiscussion'
        verbose_name_plural = 'NewsDiscussions'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.comment, self.date, self.owner, self.post)

