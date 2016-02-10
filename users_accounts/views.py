from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password

def edit_user(request):
    return redirect(reverse('home')) 

def new_user(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.password = make_password(request.POST.get('password1',))
        user.save()
        return redirect(reverse("polls:index"))

    return render(request, 'registration/new.html', {'form': form})

