from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import *

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def login_user(request):
	if request.method == 'POST':
		login = User.objects.login_user(request.POST)
		if login:
			request.session['user_id'] = login[1].id
			return redirect('/books_dashboard')
		else:
			messages.error(request, 'Invalid credentials')
	return redirect('/')

def books_new(request):
	context = {
		'authors' : Author.objects.all(),
	}
	return render(request, 'main/books_new.html', context)

def create_book(request):
	if request.method == 'POST':
		#do I need to create an author?
		if 'list_author' in request.POST and request.POST.get('new_author') != '':
			messages.error(request, 'Only one author field is allowed.')
			return redirect('/books/new')
		if 'list_author' not in request.POST:
			author = Author.objects.create(name=request.POST.get('new_author'))
		else:
			author = Author.objects.get(name=request.POST.get('list_author'))
		#create a new book
		book = Book.objects.create(
			title=request.POST.get('title'),
			author = author
		)
		#create a review
		Review.objects.create(
			review=request.POST.get('review'),
			score=request.POST.get('score'),
			book = book,
			user = User.objects.get(id=request.session['user_id'])
		)
		return redirect('/books_dashboard')
	else:
		return redirect("/books/new")

def books_show(request, id):
	context = {
		'book': Book.objects.get(id=id),
		'reviews': Review.objects.filter(book__id=id)
	}
	return render(request, 'main/books_show.html', context)

def create_review(request, id):
	if request.method == 'POST':
		Review.objects.create(
			review=request.POST.get('review'),
			score=request.POST.get('score'),
			user=User.objects.get(id=request.session['user_id']),
			book=Book.objects.get(id=id)
		)
		return redirect('/books_dashboard')
	else:
		return redirect("/books/{}".format(id))

def users_show(request, id):
	user = User.objects.annotate(review_count = Count('reviews')).get(id=id)
	context = {
		'user': user,
		'reviews': user.reviews.all()
	}
	return render(request, 'main/users_show.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

def books_dashboard(request):
	context = {
		'current_user': User.objects.get(id=request.session['user_id']),
		'recent_book_reviews': Review.objects.all().order_by('-id')[:3],
		'other_book_reviews': Review.objects.all().order_by('-id')[3:],
	}
	return render(request, 'main/books_dashboard.html', context)


