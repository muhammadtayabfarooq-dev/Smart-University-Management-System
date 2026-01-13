from django.contrib import admin

from .models import Exam, ExamResult


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('offering', 'name', 'exam_date', 'max_score')
    list_filter = ('exam_date', 'offering')


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('exam', 'enrollment', 'score', 'graded_at')
    list_filter = ('exam',)
