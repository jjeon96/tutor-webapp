from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from log.models import UserProfile
import random
from django.utils import timezone


# Create your views here.
def stub(request):
    return render(request, 'tutorapp/stub.html', {})


def login(request):
    return render(request, 'tutorapp/login.html', {})

def update(request):
    return render(request, 'updateProfile.html', {})

# def logout(request):
# 	return render(request, 'tutorapp/stub.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    if request.user.pk is None:
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'message': "Please Login or Register to look at details of the Post",'posts': posts})
    else:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', {'post': post})


def post_filter(request):
    posts = Post.objects.all()
    #TODO: Shoud do something with query
    temp_posts = posts.filter(course_name='CPSC').order_by('-created_at', '-year')
    return render(request, 'post_list.html', {'posts': temp_posts})


def post_new(request):
    if not request.user.pk is None:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                # TODO: FOLLOWINGS SHOULD BE USER LOGGED IN
                post.username = request.user
                # TODO: RANDOM BY DEFAULT
                curr_user = UserProfile.objects.get(user=request.user)
                post.year = curr_user.year_level
                post.major = curr_user.major
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    else:
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'message': "Please Login or Register to create new posts",'posts': posts})
    return render(request, 'post_edit.html', {'form': form})

def home(request):
    return render(request, 'home.html', {})

