from django import forms
from .models import Timepost

class TimepostForm(forms.ModelForm):
    class Meta:
        model = Timepost
        fields = ['student_username',
                  'tutor_pk',
                  'course_name',
                  'course_number',
                  'days',
                  'start_time',
                  'end_time',]