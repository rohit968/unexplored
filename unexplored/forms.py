from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Article

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1']

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'content', 'category')

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'shadow appearance-none'}))
	password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'shadow appearance-none'}))