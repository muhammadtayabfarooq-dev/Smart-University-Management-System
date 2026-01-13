from django.urls import path

from .views import invoice_list, payment_list

app_name = 'finance'

urlpatterns = [
    path('', invoice_list, name='invoices'),
    path('payments/', payment_list, name='payments'),
]
