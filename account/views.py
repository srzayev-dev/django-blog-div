from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

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


