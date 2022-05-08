from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
	return render(request, "blog/index.html")

#def detail(request, pk):
	#post = Post.objects.get(id=pk)
	#return render(request, "blog/article_detail.html")


def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = UserCreationForm()

	context = {
		'form':form
	}

	return render(request, "blog/signup.html", context)

def home(request):

	posts = Post.objects.all()

	context = {
		'posts':posts
	}

	return render(request, "blog/home.html", context)