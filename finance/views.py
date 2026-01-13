from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import FeeInvoice, Payment


@login_required
def invoice_list(request):
    invoices = FeeInvoice.objects.select_related('student').order_by('-created_at')
    return render(request, 'finance/invoice_list.html', {'invoices': invoices})


@login_required
def payment_list(request):
    payments = Payment.objects.select_related('invoice', 'invoice__student').order_by('-paid_at')
    return render(request, 'finance/payment_list.html', {'payments': payments})
