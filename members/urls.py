# from django.urls import path
# from .views import UserRegisterView
from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
	path('register/',views.UserRegisterView.as_view(), name='register'),

	path('editProfile/',views.UserEditView.as_view(), name='editProfile'),
	# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/changePassword.html')),
	path('password/', views.PasswordsChangeView.as_view(template_name='registration/changePassword.html')),
	path('passwordSuccess', views.passwordSuccess, name='passwordSuccess'),
	path('<slug:pk>/profile/', views.ShowProfilePageView.as_view(), name='show_profile_page'),
	path('<slug:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_profile_page'),

	
]