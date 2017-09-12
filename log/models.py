from django.db import models
from django.contrib.auth.models import User
from tutorapp.course_list import COURSE_CHOICES
from tutorapp.year_level import YEAR_LEVEL
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


#user_profile_id = models.AutoField(primary_key = True)
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=20, choices=COURSE_CHOICES,
                             default='CPSC')
    year_level = models.IntegerField(choices=YEAR_LEVEL, default=1)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00,validators=[MinValueValidator(0.00), MaxValueValidator(10.00)])
    number_of_votes = models.IntegerField(default = 0)

    # user_profile_id = models.AutoField(primary_key = True)

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.save()

        # def save(self, *args, **kwargs):
        #     u = super(User, self).save(*args, **kwargs)
        #     UserProfile.objects.get_or_create(user_id=u.id)
        #     return u

        @receiver(post_save, sender=User)
        def create_user_profile(
            sender,
            instance,
            created,
            **kwargs
            ):
            if create:
                UserProfile.objects.create(user=instance)

        @receiver(post_save, sender=User)
        def save_user_profile(sender, instance, **kwargs):
            instance.user_profile.save()



