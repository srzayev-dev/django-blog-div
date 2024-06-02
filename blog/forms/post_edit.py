from django import forms
from blog.models.post import Post

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']