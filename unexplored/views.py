from django.shortcuts import render, redirect
from .models import Article
from .forms import RegistrationForm, ArticleForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	posts = Article.objects.all()[:6]
	templateName = 'blog/index.html'
	return render(request, templateName, {'posts':posts})

@login_required
def create_post(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST or None)
		if form.is_valid():
			posts = form.save(commit=False)
			posts.user = request.user
			posts.created_date = timezone.now()
			posts.save()
			return redirect('my_post')
	else:
		form = ArticleForm()
	templateName = 'blog/create_post.html'
	return render(request, templateName, {'form':form})


def my_post(request):
	if request.user.is_authenticated:
		posts = Article.objects.filter(user=request.user)
	else:
		posts=[]
	templateName = 'blog/my_post.html'
	return render(request, templateName, {'posts':posts})

def display_post(request):
	templateName = 'blog/display_post.html'
	return render(request, templateName, {'posts':posts})

def signup(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegistrationForm()

	templateName = 'blog/signup.html'
	return render(request, templateName, {'form':form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		print(form)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			print(username)
			password = form.cleaned_data.get('password')
			print(password)
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('my_post')
		else:
			print("Invalid username or password")
	else:
		form = LoginForm()
	templateName = 'registration/login.html'
	return render(request, templateName, {'form':form})

@login_required
def logout_request(request):
	logout(request)
	template = 'blog/logout.html'
	return redirect('/')
