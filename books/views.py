from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from books.forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from books.models import Book

def books(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return render(request, 'books.html', context)


def add_book(request):
    context = {
        'bookform': BookForm(),
    }
    return render(request, 'addbook.html', context)


def add_book_action(request):
    bookform = BookForm(request.POST, request.FILES)
    if bookform.is_valid():
        bookform.save()
        return redirect('books:books')
    else:
        context = {
            'bookform': bookform,
        }
        return render(request, 'addbook.html', context)

def find_book(request):
    return HttpResponse("BOOK FOUND")




def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book_detail.html', {'book':book})

def edit(request,pk):
    book = Book.objects.get(id=pk)
    if request.POST:
        book.author = request.POST.get('author')
        book.name = request.POST.get('name')
        book.year_published = request.POST.get('year_published')
        try:
            book.save()
            messages.info(request, 'Saved successfuly!')
            return redirect('books:book_detail', book.id)
        except Exception as ex:
            messages.error(request, 'ERROR saving book!'+ str(ex))
            book = Book.objects.get(id=pk)

        
    return render(request, 'book_detail.html', {'book':book, 'edit_book': True})
    
@login_required
def delete_book(request, pk):
    if not request.user.is_staff:
        return HttpResponse('YOU ARE Not allowed to delete books')

    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('books:books')

