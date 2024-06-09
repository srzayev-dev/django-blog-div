from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from account.forms import CustomUserCreationForm, ProfilEditForm
from django.contrib.auth import authenticate, login

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='/admin/login/')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            my_user = form.save()
            update_session_auth_hash(request, my_user)
            messages.success(request, 'Şifrə uğurla dəyişdirildi!')
            return redirect('password_change')
        else:
            messages.error(request, 'Xətanı düzəldin !.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', context={'form': form})




def registerView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def profile_edit(request):
    if request.method == 'POST':
        form = ProfilEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile_edit')
    else:
        form = ProfilEditForm(instance=request.user)
    return render(request, 'profile_edit.html', context={'form': form})

