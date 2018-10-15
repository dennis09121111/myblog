from django.shortcuts import render, redirect
from .forms import UserRegisterFrom, UserUpdateFrom, ProfileUpdateFrom
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} account created successfully!")
            return redirect('user_login')
    else:
        form = UserRegisterFrom()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateFrom(request.POST, instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profil updated successfully!")
            return redirect('user_profile')
    else:
        u_form = UserUpdateFrom(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile.html', context)
