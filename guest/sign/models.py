from django.db import models
from django.db.models import Model

# Create your models here.
class Event(Model):
	name = models.CharField(max_length=100)
	limit = models.IntegerField()
	status = models.BooleanField()
	address = models.CharField(max_length=200)
	start_time = models.DateTimeField('events time')
	create_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Guest(Model):
	event = models.ForeignKey(Event)
	realname = models.CharField(max_length=64)
	phone = models.CharField(max_length=16)
	email = models.EmailField()
	sign = models.BooleanField()
	create_time = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ("event","phone")

	def __str__(self):
		return self.realname