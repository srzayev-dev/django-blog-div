from django import forms
from blog.models.category import Category

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())