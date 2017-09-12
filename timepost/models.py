from django.db import models

# Create your models here.



class Timepost(models.Model):
	student_username = models.CharField(max_length=100)
	tutor_pk = models.CharField(max_length=100)
	course_name = models.CharField(max_length = 50, default="")
	course_number = models.IntegerField()
	days = models.CharField(max_length = 10)
	start_time = models.TimeField(blank=False, null = False)
	end_time = models.TimeField(blank=False, null = False)


	def publish(self):
		self.save()

		
