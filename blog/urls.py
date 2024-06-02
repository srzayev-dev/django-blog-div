from django.contrib import admin
from django.urls import path, include

from blog.views import home, category, myPostsView, post_detail, post_create, post_edit, post_delete
urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category, name='category'),
    path('myposts/', myPostsView, name='myPosts'),
    path('detail/<slug:slug>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('edit/<slug:slug>/', post_edit, name='post_edit'),
    path('delete/<slug:slug>/', post_delete, name='post_delete'),
]