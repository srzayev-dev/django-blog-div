from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models.post import Post, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    #return HttpResponse('<h1>Hello World</h1>')
    # categories = Category.objects.all()  # Fetch all categories
    
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 2)

    context = {
        'posts': paginator.get_page(page),
        # 'categories': categories
    }
    return render(request, 'home.html', context=context)

def category(request, slug):
    # posts = Post.objects.filter(category__slug=slug)
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 1)

    context = {
        'category': category,
        'posts': paginator.get_page(page)
    }
    return render(request, 'home.html', context=context)


@login_required(login_url='/admin/login/')
def myPostsView(request):
    # posts = Post.objects.filter(author=request.user).order_by('-created_at')
    posts = request.user.postsByAuthor.all().order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 2)

    context =  {
        'posts': paginator.get_page(page)
    }
    return render(request, 'myPosts.html', context=context)


def hello_world_view(request):
    # return render(request, 'hello_world.html')
    return HttpResponse('Hello World')
