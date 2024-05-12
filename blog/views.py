from django.shortcuts import render, get_object_or_404
from blog.models.post import Post, Category
from django.core.paginator import Paginator

def home(request):
    #return HttpResponse('<h1>Hello World</h1>')
    # categories = Category.objects.all()  # Fetch all categories
    
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 1)

    context = {
        'posts': paginator.get_page(page),
        # 'categories': categories
    }
    return render(request, 'home.html', context=context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 1)

    context = {
        'category': category,
        'posts': paginator.get_page(page)
    }
    return render(request, 'home.html', context=context)

