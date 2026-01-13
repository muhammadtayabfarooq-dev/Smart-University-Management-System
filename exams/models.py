from django.db import models

from courses.models import CourseOffering, Enrollment


class Exam(models.Model):
    offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    exam_date = models.DateField()
    max_score = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return f'{self.offering} - {self.name}'


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    graded_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('exam', 'enrollment')

    def __str__(self):
        return f'{self.enrollment.student.user.username} - {self.exam.name}'
