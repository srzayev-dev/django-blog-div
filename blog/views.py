from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms.post_create import PostCreateForm
from blog.models.post import Post, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    #return HttpResponse('<h1>Hello World</h1>')
    # categories = Category.objects.all()  # Fetch all categories

    sorgu = request.GET.get('sorgu')
    posts = Post.objects.all()
    
    if sorgu:
        posts = Post.objects.filter(Q(title__icontains=sorgu) 
                                    | Q(content__icontains=sorgu)).order_by('-created_at').distinct()
        
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)

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

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context=context)


@login_required(login_url='/admin/login/')
def post_create(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = Post()
        post.title = form.cleaned_data.get('title')
        post.content = form.cleaned_data.get('content')
        post.image = form.cleaned_data.get('image')
        post.author = request.user
        post.save()
        post.category.set(form.cleaned_data.get('category'))
        return redirect('myPosts')
          
    context = {
        'form': form,
    }
    return render(request, 'post_create.html', context=context)
