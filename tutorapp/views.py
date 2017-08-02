from django.shortcuts import render
from django.utils import timezone
#from .models import #.....  (user)
#from .models import #..... (Post)

# Create your views here.
# <<<<<<< HEAD
# def stub(request):
#     return render(request, 'tutorapp/stub.html', {})

# def post_list(request):
# 	posts = Post.objects.filter(posted_date_lte=timezone.now()).order_by('posted_date')
# 	return render(request, 'tutorapp/post_list.html', {'posts':posts})

# def register(request):
# 	return render(request, 'tutorapp/register.html',{})

# def login(request):
# 	return render(request, 'tutorapp/login.html', {})

# def omfg(request):
# 	return render(request, 'tutorapp/omfg.html',{})
# =======
def home(request):
    return render(request, 'home.html', {})

