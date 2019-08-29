from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Classroom(models.Model):
	name = models.CharField(max_length=50)
	subject = models.CharField(max_length=100)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})



class Student(models.Model):

	name = models.CharField(max_length=50)
	date_of_birth = models.DateField()

	GENDER_CHOICES = (('Female', 'Female'),('Male', 'Male'),)

	gender = models.CharField(max_length=50, choices=GENDER_CHOICES,default='Female',)
	exam_grade = models.IntegerField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


	def __str__(self):
		return self.name