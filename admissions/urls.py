from django.urls import path

from .views import application_list, apply

app_name = 'admissions'

urlpatterns = [
    path('', application_list, name='list'),
    path('apply/', apply, name='apply'),
]
