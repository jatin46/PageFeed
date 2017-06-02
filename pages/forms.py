from django import forms
from .models import UserPage, Post

class PageForm(forms.ModelForm):
	class Meta:
		model = UserPage
		exclude = ['user']
		fields = [
			"page_name",
			"cover_page",
			"category"
		]
		
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['user']
		fields = [
			"image",
			"caption"
		]
		