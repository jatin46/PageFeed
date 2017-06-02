from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from pages.models import Post

# Create your models here.

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)	
	#post = models.ForeignKey(Post)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey('content_type', 'object_id')

	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.user.username)