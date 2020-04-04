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

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		