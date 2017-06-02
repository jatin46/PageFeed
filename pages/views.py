from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .models import Post, UserPage
from django.contrib import messages
from comments.forms import CommentForm
from comments.models import Comment
from .forms import PageForm, PostForm

# Create your views here.
def index(request,	template='pages/index.html', 
	page_template='pages/post_list.html'):
	post = Post.objects.all().order_by('-time')


	if request.is_ajax():
		template = page_template

	#comments = None
	if request.user.is_authenticated():
		pk = request.user.id
		current_user = User.objects.get(id=pk)
		user_pages_list = current_user.userpage_set.all()
	else:
		user_pages_list=None

	'''if request.is_ajax():
					post_id = request.GET['post_contents_id']
					print(post_id)
					content_type = ContentType.objects.get_for_model(Post)
					obj_id = post_id
					comments = Comment.objects.filter(content_type = content_type, object_id = obj_id)
					print(comments)'''
	category = UserPage.objects.all()
	context = {
		'post' : post,
		'category' :category,
		'user_pages_list' : user_pages_list,
		'page_template': page_template,
		#'comments' : comments
	}
	return render(request, template, context)


def comment(request, post_id):
	#post_id = None
	'''if request.method == 'GET':
					post_id = request.GET['post_contents_id']'''
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			print("comment_form.cleaned_data")
			instance = form.save(commit = False)
			instance.user = User.objects.get(id=request.user.id)
			instance.save()
	else:
		comment_form = CommentForm()

	content_type = ContentType.objects.get_for_model(Post)
	obj_id = post_id
	comments = Comment.objects.filter(content_type = content_type, object_id = obj_id)
	context = {
		'comments' : comments,
		'comment_form' : comment_form,
		'post_id' : post_id,
	}
	print(comments)
	return render(request, 'pages/comments.html', context)

def  browse(request):
	page_list = UserPage.objects.all()
	context = {
		'page_list' : page_list,
	}
	return render(request, 'pages/browse.html', context)

def	pageDetail(request, page_id):
	try:
		userpage = UserPage.objects.get(pk=page_id)
	except UserPage.DoesNotExist:
		raise Http404("Page Does Not Exist")

	if request.method == 'POST':
		form = PostForm(request.POST , request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.userpage = UserPage.objects.get(id=page_id)
			instance.save()
	else:
		form = PostForm()

	user_post_list = userpage.post_set.all()

	context = {
		'userpage' : userpage,
		'form' : form,
		'user_post_list' :user_post_list
	}
	return render(request, 'pages/pagedetail.html', context)

def create(request):
	if request.user.is_authenticated():
		if request.method=='POST':
			form = PageForm(request.POST , request.FILES)
			if form.is_valid():
				instance = form.save(commit = False)
				instance.user = User.objects.get(id=request.user.id)
				instance.save()
				return redirect('pagedetail', page_id=instance.id)
		else:
			form = PageForm()
		context = {
			"form" : form,
		}
		return render(request, 'pages/create.html', context)
	else:
		messages.error(request, "please Login First")
		return HttpResponseRedirect(reverse('index'))


\