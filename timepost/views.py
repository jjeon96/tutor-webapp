from django.shortcuts import render
from .models import Timepost
from log.models import UserProfile
from tutorapp.models import Post


# Create your views here.


def timepost_create(request):
	