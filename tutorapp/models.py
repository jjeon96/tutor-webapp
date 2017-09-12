from django.db import models
from .course_list import COURSE_CHOICES
from django.utils import timezone
from log.models import UserProfile


# Create your models here.


class Post(models.Model):

    userpk = models.CharField(max_length=100, default='error')

    course_name = models.CharField(max_length=50, choices=COURSE_CHOICES)
    course_number = models.IntegerField()
    start_at = models.DateTimeField(default=timezone.now)
    end_at = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=200, default="Not specified")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.save()

    def __str__(self):
        if self.userpk == 'error':
            return "Invalid Post: No userpk"
        user = UserProfile.objects.get(pk=self.userpk)
        name = user.user.username
        year = user.get_year_level_display()
        return "Date: " + str(self.created_at.date()) + " " + name + " Year:" + str(year)
