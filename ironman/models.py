from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=50)
	job = models.CharField(max_length=50)

	def __str__(self):
		return '{0} {1}'.format(self.name, self.job)