from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class UserPage(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cover_page = models.FileField()
	page_name = models.CharField(max_length=250)
	category = models.CharField(max_length=250)

	def get_absolute_url(self):
		reverse('pagedetail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.page_name


class Post(models.Model):
	userpage = models.ForeignKey(UserPage, on_delete = models.CASCADE)
	image=models.FileField()
	time = models.DateTimeField(default=timezone.now)
	caption=models.CharField(max_length=250,blank=True)

	def __str__(self):
		return str(self.image)



		

		
