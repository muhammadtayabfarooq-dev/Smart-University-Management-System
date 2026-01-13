from django.urls import path

from .views import exam_list, result_list

app_name = 'exams'

urlpatterns = [
    path('', exam_list, name='list'),
    path('results/', result_list, name='results'),
]
