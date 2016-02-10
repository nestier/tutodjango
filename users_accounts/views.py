from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def new_user(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.password = make_password(request.POST.get('password1',))
        user.save()
        return redirect(reverse("polls:index"))

    return render(request, 'registration/new.html', {'form': form})

@login_required
def edit_user(request):
    user = get_object_or_404(User, pk = request.session['_auth_user_id'])
    form = UserRegisterForm(request.POST or None, instance = user)
    if form.is_valid():
        request.POST['password'] = make_password(request.POST.get('password1'))
        user = form.save(commit=False)
        return redirect(reverse("polls:index"))

    return render(request,'registration/edit.html', {'form': form}) 


