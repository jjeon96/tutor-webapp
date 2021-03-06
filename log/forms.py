# from django.contrib.auth.forms import AuthenticationForm 
# from django import forms

# # If you don't do this you cannot use Bootstrap CSS
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label="Username", max_length=30, 
#                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
#     password = forms.CharField(label="Password", max_length=30, 
#                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
from django import forms
from tutorapp.course_list import COURSE_CHOICES
from .models import UserProfile
from tutorapp.year_level import YEAR_LEVEL
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

           

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
             
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'first_name',
            'last_name',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

class ProfileRegistrationFrom(forms.ModelForm):
    major = forms.CharField(widget=forms.Select(choices=COURSE_CHOICES))
    year_level = forms.CharField(widget=forms.Select(choices=YEAR_LEVEL))

    class Meta:
        model = UserProfile
        fields = [
            'major',
            'year_level'
        ]


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]



class ProfileEditForm(forms.ModelForm):
    major = forms.CharField(widget=forms.Select(choices=COURSE_CHOICES))
    year_level = forms.CharField(widget=forms.Select(choices=YEAR_LEVEL))

    class Meta:
        model = UserProfile
        fields = [
            'major',
            'year_level'
        ]










