from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, SearchForm
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
    posts = Post.objects.all().order_by('-updated_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    if request.user.pk is None:
        posts = Post.objects.all()
        return render(request, 'post_list.html',
                      {'message': "Please Login or Register to look at details of the Post", 'posts': posts})
    else:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', {'post': post})


# TODO: posting should be valid only when user is logged in
def post_new(request):
    if not request.user.pk is None:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)

                post.username = request.user
                curr_user = UserProfile.objects.get(user=request.user)
                post.name = request.user.first_name + request.user.last_name
                post.year = curr_user.year_level
                post.major = curr_user.major
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    else:
        posts = Post.objects.all()
        return render(request, 'post_list.html',
                      {'message': "Please Login or Register to create new posts", 'posts': posts})
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            curr_user = UserProfile.objects.get(user=request.user)
            post.name = request.user.first_name + " " + request.user.last_name
            post.year = curr_user.year_level
            post.major = curr_user.major
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def my_post(request):
    # TODO: Shoud do something with query
    posts = Post.objects.all()
    posts = posts.filter(username=request.user).order_by('-updated_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_search(request):
    if request.GET.__len__() != 0:
        form = SearchForm(request.GET)
        if form.is_valid():
            posts = Post.objects.all()
            query = request.GET
            posts = posts.filter(course_name=query.get('course_name'), course_number=query.get('course_number'))
            return render(request, 'post_list.html', {'posts': posts})
    else:
        form = SearchForm()
    return render(request, 'post_search.html', {'form': form})


def search_result(request, posts):
    return render(request, 'post_list.html', {'posts': posts})


def home(request):
    if request.GET.__len__() != 0:
        form = SearchForm(request.GET)
        if form.is_valid():
            posts = Post.objects.all()
            query = request.GET
            posts = posts.filter(course_name=query.get('course_name'), course_number=query.get('course_number'))
            return render(request, 'post_list.html', {'posts': posts})
    else:
        form = SearchForm()
    return render(request, 'home.html', {'form': form})
