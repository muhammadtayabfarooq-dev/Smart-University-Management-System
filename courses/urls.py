from django.urls import path

from .views import course_list, enrollment_list, offering_list

app_name = 'courses'

urlpatterns = [
    path('', course_list, name='list'),
    path('offerings/', offering_list, name='offerings'),
    path('enrollments/', enrollment_list, name='enrollments'),
]
