from django.urls import path, include

from account.views import logout_view, password_change, registerView, profile_edit

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('password_change/', password_change, name='password_change'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', registerView, name='register'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    
]