from django.db import models
from blog.models.category import Category
from autoslug import AutoSlugField
#from django.contrib.auth.models import User
from account.models import CustomUser
 

class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='posts')
    slug = AutoSlugField(populate_from='title', unique=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='postsByAuthor')

    def __str__(self): 
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'posts'