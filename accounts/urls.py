from django.urls import path

from .views import UMSLoginView, UMSLogoutView, register

urlpatterns = [
    path('login/', UMSLoginView.as_view(), name='login'),
    path('logout/', UMSLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
