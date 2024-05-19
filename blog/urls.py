from django.contrib import admin
from django.urls import path, include

from blog.views import home, category, myPostsView, hello_world_view
urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category, name='category'),
    path('myposts/', myPostsView, name='myPosts'),
    path('hello/', hello_world_view, name='hello'),
]