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
    LEVEL = (
        ('Associate degree', 'Associate degree'),
        ('Bachelor degree', 'Bachelor degree'),
        ('Master degree', 'Master degree'),
        ('Doctoral degree', 'Doctoral degree'),
    )
    level = models.CharField(choices=LEVEL, max_length=200)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.first_name, self.last_name, self.username, self.mobile)


class Student(UserAbstract):
    STAGE = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior')
    )
    stage = models.CharField(choices=STAGE, max_length=200, default='Freshman')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.first_name, self.last_name, self.username, self.mobile)


class ProfileAbstract(models.Model):
    email = models.EmailField()
    bio = models.TextField(max_length=200)

    class Meta:
        abstract = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{}: {}'.format(self.email, self.bio)


class TeacherProfile(ProfileAbstract):
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{}:'.format(self.user)


class LowGpaStudents(models.Manager):
    def low_gpa_students(self):
        return super().get_queryset().filter(gpa=2)


class MediumGpaStudents(models.Manager):
    def medium_gpa_students(self):
        return self.filter(gpa=3)


class HighGpaStudents(models.Manager):
    def high_gpa_students(self):
        return self.filter(gpa=4)


class StudentProfile(ProfileAbstract):
    gpa = models.IntegerField(default=0)
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    objects = models.Manager()
    low_gpa_students = LowGpaStudents()
    medium_gpa_students = MediumGpaStudents()
    high_gpa_students = HighGpaStudents()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{}:'.format(self.user)