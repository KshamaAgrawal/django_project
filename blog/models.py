from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse

class Post(models.Model):
	author         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title          = models.CharField(max_length=160)
	slug           = models.SlugField(max_length = 160, null = True, unique = True)
	text           = models.TextField()
	created_date   = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)	

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title	

	def get_absolute_url(self):
		return "/post/%i" % self.id

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug': self.slug})
				