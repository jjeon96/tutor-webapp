from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, ProfileRegistrationFrom, UserEditForm, ProfileEditForm
from django.core.mail import send_mail 
from django.http import HttpResponse
from django.core.mail import EmailMessage
from log.models import UserProfile

# @login_required(login_url="login/")
# def home(request):
#     return render(request,"home.html")

def login_view(request):
    if request.user.pk:
        return redirect('/')
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
        # return render(request,"home.html")
    return render(request, "login.html", {"form":form, "title": title})


def register_view(request):
    if request.user.pk:
        return redirect('/')
    else:
        print(request.user.is_authenticated())
        title = "Register"
        user_form = UserRegisterForm(request.POST or None)
        profile_form = ProfileRegistrationFrom(request.POST or None)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            first_name = user_form.cleaned_data.get('first_name')
            last_name = user_form.cleaned_data.get('last_name')
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile = profile_form.save(commit= False)
            profile.user = user

            profile_form.save()
            sendSimpleEmail(request, user.email)
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return redirect("/")

        context = {
            "user_form": user_form,
            "profile_form": profile_form,
            "title": title
        }
        return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/login")


def sendSimpleEmail(request,emailto):
	#   send_mail('Email Title','Email Message','from@example.com',['to@example.com'])
    res = send_mail("Thank you for joining MentorUs!", "Thanks", "donotrespond.mentor.us@gmail.com",[emailto])
    return HttpResponse('%s'%res)


def update_view(request):
    if request.user.pk is None:
        return redirect('/')
    else:
        profile_user = UserProfile.objects.get(user=request.user)
        user_edit_form = UserEditForm(request.POST or None,
                                      initial={'first_name': request.user.first_name,
                                               'last_name':request.user.last_name, 'email':request.user.email})
        profile_edit_form = ProfileEditForm(request.POST or None, initial={'major':profile_user.major, 'year_level':profile_user.year_level})
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            # user_name = user_edit_form.cleaned_data.get('username')
            user = user_edit_form.save(commit=False)
            first_name = user_edit_form.cleaned_data.get('first_name')
            last_name = user_edit_form.cleaned_data.get('last_name')
            email = user_edit_form.cleaned_data.get('email')
            # if (user_name != request.user.username) :
            #     request.user.username = user_name
            if (request.user.email != email):
                request.user.email = email

            request.user.first_name = first_name
            request.user.last_name = last_name
            profile_user.major = profile_edit_form.cleaned_data.get('major')
            profile_user.year_level = profile_edit_form.cleaned_data.get('year_level')

            request.user.save()
            profile_user.save()

            new_user = authenticate(username=request.user.username, password=request.user.password)
            login(request, new_user)
            return redirect('/')

        context = {
            "user_edit_form": user_edit_form,
            "profile_edit_form": profile_edit_form,
            "title": "Edit Profile"
        }
    return render(request, "updateProfile.html", context)







