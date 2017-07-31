from django.shortcuts import render
from .models import Post


# Create your views here.
def stub(request):
    return render(request, 'tutorapp/stub.html', {})


def login(request):
    return render(request, 'tutorapp/login.html', {})


# def logout(request):
# 	return render(request, 'tutorapp/stub.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
