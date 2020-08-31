from django.urls import path
from . import views
from .views import HomeView, CreatePostView, PostDetailView, \
					PostDeleteView, SignUpView, UserLoginView, UserLogoutView

urlpatterns = [
	path('', HomeView.as_view(), name='index'),
	path('create_post', CreatePostView.as_view(), name='create_post'),
	path('display_post/', views.display_post, name='display_post'),
	path('post_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
	path('post_detail/<int:pk>/post_edit', views.post_edit, name='post_edit'),
	path('post_detail/<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
	path('my_post/', views.my_post, name='my_post'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('login', UserLoginView.as_view(), name='login'),
	path('logout', UserLogoutView.as_view(), name='logout'),
]