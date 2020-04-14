from django.db import models
from django.contrib.auth.models import AbstractUser

# from core.models import Class


class MyUser(AbstractUser):
    pass


class User(MyUser):
    USER_ROLES = (
        ('admin', 'admin'),
        ('teacher', 'teacher'),
        ('student', 'student'),
    )
    role = models.CharField(choices=USER_ROLES,max_length=200)
    mobile = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        abstract = True

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.first_name, self.last_name, self.username, self.role, self.mobile)


class Student(User):
    # classes = models.ForeignKey(Class, related_name='classes')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.first_name, self.last_name, self.username, self.role, self.age)


class Teacher(User):
    LEVEL = (
        ('Associate degree', 'Associate degree'),
        ('Bachelor degree', 'Bachelor degree'),
        ('Master degree', 'Master degree'),
        ('Doctoral degree', 'Doctoral degree'),
    )
    status = models.CharField(choices=LEVEL, max_length=200, default='Associate degree')
    studenty = models.ForeignKey(Student, models.SET_NULL, blank=True, null=True, related_name='studenty')
    # classes = models.ForeignKey(Class, related_name='classes')

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.first_name, self.last_name,  self.username, self.role, self.status)

