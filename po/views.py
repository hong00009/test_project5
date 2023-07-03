from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }

    return render(request, 'po/index.html', context)

@login_required
#비로그인 상태에서 글쓰기 하면, user 정보를 확인할 수 없다며 24번줄에서 에러남
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('po:index')
        
    else:
        form = PostForm()

    context = {
        'form' : form,
    }

    return render(request, 'po/form.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post' : post,
    }

    return render(request, 'po/detail.html', context)