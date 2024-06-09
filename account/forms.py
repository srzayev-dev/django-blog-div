from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from account.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ProfilEditForm(UserChangeForm):
     password = None
     class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_picture', ]
