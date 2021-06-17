from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book, Borrower
from .forms import EditBookForm, AddBookForm

def login(request):
    return render(request, 'lib_man/login.html')

def lib_search(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'lib_man/library_search.html', context)

def dashboard(request):
    return render(request, 'lib_man/portalPages/dashboard.html')

def books(request):
    context = {
        'books': Book.objects.all(),
        'edit_book_form': EditBookForm(),
        'add_book_form': AddBookForm()
    }
    return render(request, 'lib_man/portalPages/books.html', context)

def borrowers(request):
    context = {
        'borrowers': Borrower.objects.all()
    }
    return render(request, 'lib_man/portalPages/borrowers.html', context)

def borrowed_books(request):
    return render(request, 'lib_man/portalPages/borrowed_books.html')

# Functions

def edit_book(request):
    book = Book.objects.get(pk = request.POST.get('pk'))
    book.title = request.POST.get('title')
    book.author = request.POST.get('author')
    book.isbn = request.POST.get('isbn')
    book.publisher = request.POST.get('publisher')
    book.genre = request.POST.get('genre')
    book.book_location = request.POST.get('book_location')
    if request.POST.get('status_borrowed') == 'on':
        book.status_borrowed = True
    else:
        book.status_borrowed = False
    book.save()
    return HttpResponseRedirect('admin/books')

def add_book(request):
    status_borrowed = True
    if request.POST.get('status_borrowed') == 'on':
        status_borrowed = True
    else:
        status_borrowed = False
    book = Book.objects.create(
        title=request.POST.get('title'),
        author=request.POST.get('author'),
        isbn=request.POST.get('isbn'),
        publisher=request.POST.get('publisher'),
        genre=request.POST.get('genre'),
        book_location=request.POST.get('book_location'),
        status_borrowed=status_borrowed
    )
    return HttpResponseRedirect('admin/books')

def delete_book(request):
    book = Book.objects.get(pk = request.POST.get('pk'))
    book.delete()
    return HttpResponseRedirect('admin/books')