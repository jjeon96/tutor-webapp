from django import forms
from .course_list import COURSE_CHOICES
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('course_name', 'course_number', 'start_at', 'end_at', 'comment')
        widgets = {
            # TODO: Hope these in html ui to be date/time picker (maybe using angular.js/JQuery)
            'start_at': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'end_at': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }


class SearchForm(forms.Form):
    # TODO: Search form must be specified
    CREATED_ORDER_CHOICE = (('-created_at', 'Most Recent',), ('created_at', 'Oldest'),)

    course_name = forms.ChoiceField(required=False, choices=COURSE_CHOICES)
    course_number = forms.IntegerField(required=False)
    created_date_order = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=CREATED_ORDER_CHOICE,)
