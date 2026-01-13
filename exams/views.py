from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Exam, ExamResult


@login_required
def exam_list(request):
    exams = Exam.objects.select_related('offering', 'offering__course', 'offering__term').order_by('-exam_date')
    return render(request, 'exams/exam_list.html', {'exams': exams})


@login_required
def result_list(request):
    results = ExamResult.objects.select_related('exam', 'enrollment', 'enrollment__student').order_by('-graded_at')
    return render(request, 'exams/result_list.html', {'results': results})
