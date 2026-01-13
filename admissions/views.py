from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AdmissionApplicationForm
from .models import AdmissionApplication


@login_required
def application_list(request):
    applications = AdmissionApplication.objects.order_by('-submitted_at')
    return render(request, 'admissions/application_list.html', {'applications': applications})


@login_required
def apply(request):
    if request.method == 'POST':
        form = AdmissionApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admissions:list')
    else:
        form = AdmissionApplicationForm()
    return render(request, 'admissions/apply.html', {'form': form})
