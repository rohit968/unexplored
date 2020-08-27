from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('create_post/', views.create_post, name='create_post'),
	path('display_post/', views.display_post, name='display_post'),
	path('my_post/', views.my_post, name='my_post'),
	path('signup/', views.signup, name="signup"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout_request, name='logout'),
]