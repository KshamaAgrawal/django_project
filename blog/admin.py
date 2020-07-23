from django.contrib import admin
from .models import Post 
from django.db import models



class postAdmin(admin.ModelAdmin):
	# fieldsets = [
 #      (None, {
 #          'fields': [('title', 'text'), 'created_date']
 #      })
 #   ]

	list_display = ('author', 'title' , 'text' , 'created_date')
	search_fields=['title' , 'text']
	# ordering = ('title')
	

admin.site.register(Post,postAdmin)
