from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	itemname = models.CharField(max_length=100)
	#creator = request.session['user.id']
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
