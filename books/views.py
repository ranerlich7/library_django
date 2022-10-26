from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
 
def books(request):
   context = {
       'book_list': ['Harry Potter','Lord of the Rings','Hobbit'],
   }
   return render(request, 'books.html', context)

def add_book(request):
    return HttpResponse("BOOK ADDED")

def find_book(request):
    return HttpResponse("BOOK FOUND")

def delete_book(request):
    return HttpResponse("BOOK DELETED")
