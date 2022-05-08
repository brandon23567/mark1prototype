from django.db import models

# Create your models here.

class Post(models.Model):
	author = models.CharField(max_length=20)
	heading = models.CharField(max_length=20)
	post_image = models.ImageField(blank=True, null=True, upload_to="images/")
	body = models.TextField()
	summary = models.CharField(max_length=255)
	date_posted = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.heading