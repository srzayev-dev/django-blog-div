from django.contrib import admin
from django.urls import path, include

from blog.views import home, category
urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category, name='category'),
]