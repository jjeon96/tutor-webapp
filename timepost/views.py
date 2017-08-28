from django.shortcuts import render
from .models import Timepost
from log.models import UserProfile
from tutorapp.models import Post
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import TimepostForm


# Create your views here.


def timepost_create(request):
        student_username = request.GET.get("student_username", None)
        tutor_pk = request.GET.get("tutor_pk", None)
        course_name = request.GET.get("course_name", None)
        course_number = request.GET.get("course_number", None)
        days = request.GET.get("days", None)
        start_time = request.GET.get("start_time", None)
        end_time = request.GET.get("end_time", None)

        timepost = TimepostForm(request or None)
        timepost['student_username'] = student_username
        timepost['tutor_pk'] = tutor_pk
        timepost['course_name'] = course_name
        timepost['course_number'] = course_number
        timepost['days'] = days
        timepost['start_time'] = start_time
        timepost['end_time'] = end_time
        timepost.save()



