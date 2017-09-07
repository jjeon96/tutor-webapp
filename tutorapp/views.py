from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, SearchForm
from log.models import UserProfile
from django.db import models
from django.contrib.auth.models import User
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
    pairs = pair_creator(request, posts)

    return render(request, 'post_list.html', {'posts': pairs})


def post_detail(request, pk):
    if request.user.pk is None:
        posts = Post.objects.all()
        return render(request, 'post_list3.html')
    else:
        post = get_object_or_404(Post, pk=pk)
        if post.userpk == -1:
            referer = request.META.get('HTTP_REFERER', '')
            return redirect(referer)
        author = get_object_or_404(UserProfile, pk=post.userpk)

        return render(request, 'post_detail.html', {'post': post, 'author': author})


# TODO: posting should be valid only when user is logged in
def post_new(request):
    if not request.user.pk is None:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.userpk = request.user.pk
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    else:
        posts = Post.objects.all()
        return render(request, 'post_list3.html', {'posts': posts})
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if post.userpk == 'error':
                post.userpk = request.user.pk
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def my_post(request):
    # TODO: Shoud do something with query

    pairs = []
    author = get_object_or_404(UserProfile, pk=request.user.pk)
    posts = Post.objects.filter(userpk=request.user.pk).order_by('-updated_at')
    for post in posts:
        pairs.append({'post': post, 'author': author})

    return render(request, 'post_list.html', {'posts': pairs})


def post_search(request):
    if request.GET.__len__() != 0:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = request.GET
            posts = Post.objects.filter(course_name=query.get('course_name'), course_number=query.get('course_number'))
            pairs = pair_creator(request, posts)
            return render(request, 'post_list.html', {'posts': pairs})
    else:
        form = SearchForm()
    return render(request, 'post_search.html', {'form': form})


def search_result(request, posts):
    pairs = pair_creator(request, posts)
    return render(request, 'post_list.html', {'posts': pairs})


def home(request):
    if request.GET.__len__() != 0:
        form = SearchForm(request.GET)
        if form.is_valid():
            posts = Post.objects.all()
            query = request.GET
            posts = posts.filter(course_name=query.get('course_name'), course_number=query.get('course_number'))
            pairs = pair_creator(request, posts)
            return render(request, 'post_list.html', {'posts': pairs})
    else:
        form = SearchForm()
    return render(request, 'home.html', {'form': form})


def pair_creator(request, posts):
    pairs = []
    for post in posts:
        author = get_object_or_404(UserProfile, pk=post.userpk)
        pairs.append({'post': post, 'author': author})
    return pairs
