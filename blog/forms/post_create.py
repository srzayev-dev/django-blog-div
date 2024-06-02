from django import forms
from blog.models.category import Category
from blog.models.post import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']
        
        
