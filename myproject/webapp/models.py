from django.db import models
from django.core.validators import MaxValueValidator

class Register(models.Model):
	User_Name = models.CharField(max_length=50, null=True)
	First_Name = models.CharField(max_length=50, null=True)
	Last_Name = models.CharField(max_length=50, null=True)
	Password = models.CharField(max_length=100)
	Date_Join = models.DateTimeField(auto_now_add=True, blank=True)
	Email = models.EmailField(null=False, blank=False)
	def __str__(self):
		return self.First_Name
	
class Feedback(models.Model):
	Username = models.CharField(max_length=50, null=True)
	Email_Address = models.EmailField(null=False, blank=False)
	Phone_Number = models.IntegerField( blank=False)
	Feed = models.CharField(max_length=500, null=False, blank=False)
	def __str__(self):
		return self.Username
	
class MoodModel(models.Model):
	mood = models.CharField(max_length=500, null=True)
	def __str__(self):
		return self.mood