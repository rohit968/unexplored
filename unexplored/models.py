from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	title = models.CharField(max_length=200, unique=True)
	content = models.TextField()
	category = models.CharField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Article'
		ordering = ('-created_date',)

