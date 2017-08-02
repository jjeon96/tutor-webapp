from django.db import models
from .course_list import COURSE_CHOICES
from django.utils import timezone

# Create your models here.

YEAR_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)


class Post(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    course_name = models.CharField(max_length=50, choices=COURSE_CHOICES)
    course_number = models.IntegerField()
    available_date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "Date: " + str(self.created_date.date()) + " " + self.name + " Year:" + str(self.year)
