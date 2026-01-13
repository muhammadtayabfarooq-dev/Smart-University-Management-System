from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STUDENT = 'student', 'Student'
        FACULTY = 'faculty', 'Faculty'
        STAFF = 'staff', 'Staff'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=30, unique=True)
    program = models.CharField(max_length=120)
    year = models.PositiveSmallIntegerField(default=1)
    admission_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.program}'


class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    employee_id = models.CharField(max_length=30, unique=True)
    department = models.CharField(max_length=120)
    designation = models.CharField(max_length=120, blank=True)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.department}'
