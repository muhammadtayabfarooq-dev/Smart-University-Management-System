from django.contrib import admin

from .models import FeeInvoice, Payment


@admin.register(FeeInvoice)
class FeeInvoiceAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'amount', 'status', 'due_date')
    list_filter = ('status', 'due_date')
    search_fields = ('student__user__username', 'title')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'method', 'paid_at')
    list_filter = ('method', 'paid_at')
