# Imports
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Views
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.success(request, f'Cuenta creada exitosamente')
            return redirect('login')                
    else:
        form = UserRegisterForm()
        
    return render(request, 'user/register.html', {'form': form}) 

@login_required
def profile(request):
    if request.method == 'POST':
        u_update_form = UserUpdateForm(request.POST, instance=request.user)
        p_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_update_form.is_valid() and p_update_form.is_valid():
            u_update_form.save()
            p_update_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')        
    else:
        u_update_form = UserUpdateForm(instance=request.user)
        p_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_update_form': u_update_form,
        'p_update_form': p_update_form,
    }

    return render(request, 'user/profile.html', context)