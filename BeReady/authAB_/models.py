from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass


class UserAbstract(MyUser):
    mobile = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        abstract = True

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.first_name, self.last_name, self.username, self.mobile)


class Teacher(UserAbstract):
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.first_name, self.last_name, self.username, self.mobile)


class Student(UserAbstract):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.first_name, self.last_name, self.username, self.mobile)

