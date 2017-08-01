from django import forms
from django.utils import timezone
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('course_name', 'course_number', 'start_at', 'end_at',)
        widgets = {
            'start_at': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'end_at': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }
