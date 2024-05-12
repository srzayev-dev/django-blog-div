from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True, default='')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'catigories'