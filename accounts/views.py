from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import UserRegisterForm


class UMSLoginView(LoginView):
    template_name = 'accounts/login.html'


class UMSLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('dashboard:home')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
