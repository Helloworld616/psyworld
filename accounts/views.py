from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})
