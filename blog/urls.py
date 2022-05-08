from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('home/', views.home, name="home"),
	path('signup/', views.signup, name="signup"),
	#path('detail/<str:pk>/', views.detail, name="detail"),
]