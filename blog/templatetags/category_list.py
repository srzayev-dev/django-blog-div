from django import template
from blog.models.category import Category

register = template.Library()

@register.simple_tag
def category_list():
    categories = Category.objects.all()
    return categories