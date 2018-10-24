from django.db import models

# Create your models here.
class Fruit(models.Model):
	fruit_name = models.CharField(max_length=150, blank=False, unique=True)
	
	def __str__(self):
		return "{}".format(self.fruit_name)