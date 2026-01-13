from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Course, CourseOffering, Enrollment


@login_required
def course_list(request):
    courses = Course.objects.order_by('code')
    return render(request, 'courses/course_list.html', {'courses': courses})


@login_required
def offering_list(request):
    offerings = CourseOffering.objects.select_related('course', 'term', 'faculty').order_by('-term__start_date')
    return render(request, 'courses/offering_list.html', {'offerings': offerings})


@login_required
def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'offering').order_by('-enrolled_at')
    return render(request, 'courses/enrollment_list.html', {'enrollments': enrollments})
