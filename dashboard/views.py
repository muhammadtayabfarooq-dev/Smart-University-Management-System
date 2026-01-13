from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from admissions.models import AdmissionApplication
from courses.models import Course, CourseOffering, Enrollment
from exams.models import Exam, ExamResult
from finance.models import FeeInvoice, Payment


@login_required
def home(request):
    context = {
        'total_courses': Course.objects.count(),
        'total_offerings': CourseOffering.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
        'total_exams': Exam.objects.count(),
        'total_results': ExamResult.objects.count(),
        'total_invoices': FeeInvoice.objects.count(),
        'total_payments': Payment.objects.count(),
        'recent_admissions': AdmissionApplication.objects.order_by('-submitted_at')[:5],
        'recent_invoices': FeeInvoice.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard/home.html', context)
