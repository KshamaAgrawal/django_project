from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

class Post(models.Model):
	author         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title          = models.CharField(max_length=160)
	slug           = AutoSlugField(populate_from='title')
	text           = models.TextField()
	created_date   = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)	

	def my_slugify_function(content):
		return content.replace('_', '-').lower()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title	

	def get_absolute_url(self):
		return "/post/%i" % self.id

					