from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import RegistrationForm, ArticleForm, LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView


# Create your views here.

class HomeView(TemplateView):
	template_name = 'blog/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = Article.objects.all()[:6]
		return context


class CreatePostView(CreateView):
	model = Article
	template_name = 'blog/create_post.html'
	form_class = ArticleForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()

		return redirect('my_post')


def my_post(request):
	if request.user.is_authenticated:
		posts = Article.objects.filter(user=request.user)
	else:
		posts = []
	templateName = 'blog/my_post.html'
	return render(request, templateName, {'posts': posts})


def display_post(request):
	templateName = 'blog/display_post.html'
	return render(request, templateName, {'posts': posts})


class PostDetailView(DetailView):
	model = Article
	template_name = 'blog/post_detail.html'
	context_object_name = 'posts'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = get_object_or_404(Article, pk=self.kwargs.get('pk'))
		context['user'] = self.request.user
		return context



@login_required
def post_edit(request, pk):
	post = get_object_or_404(Article, pk=pk)
	form = ArticleForm(request.POST, instance=post)
	templateName = 'blog/post_edit.html'
	return render(request, templateName, {'form':form})


class PostDeleteView(DeleteView):
	model = Article
	template_name = 'blog/article_confirm_delete.html'
	success_url = '/my_post'


class SignUpView(CreateView, SuccessMessageMixin):
	template_name = 'blog/signup.html'
	success_url = '/login'
	form_class = RegistrationForm
	success_message = 'Your profile is created successfully'


class UserLoginView(LoginView):
	form_class = LoginForm
	template_name = 'registration/login.html'

	def form_valid(self, form):
		login(self.request, form.get_user())


class UserLogoutView(LogoutView):
	template_name = 'blog/logout.html'

	def get(self, request, **kwargs):
		logout(request)
		return redirect('/')

