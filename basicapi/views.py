from django.shortcuts import render
from django.http import JsonResponse
from books.models import Book

def basicbooks(request):
    books = Book.objects.all()
    booksjson = []
    for book in books:
        book = {
            "id" : 1,
            "name" : book.name,
            "author": book.author,
            "year_published": book.year_published
        }
        booksjson.append(book)
    return JsonResponse({"books": booksjson})

def book(request, pk):
    book = Book.objects.get(id=pk)
    return JsonResponse(book.json())



#   "products": [
#     {
#       "id": 1,
#       "title": "iPhone 9",
#       "description": "An apple mobile which is nothing like apple",
#       "price": 549,
#       "discountPercentage": 12.96,
#       "rating": 4.69,
#       "stock": 94,
#       "brand": "Apple",
#       "category": "smartphones",
#       "thumbnail": "...",
#       "images": ["...", "...", "..."]
#     },
#     {...},
#     {...},
#     {...}
#     // 30 items
#   ],

#   "total": 100,
#   "skip": 0,
#   "limit": 30
# }

#     usage = ['GET \ usage', 
#     'GET \books book list',
#     'GET \books\[id] single book']
#     return JsonResponse(usage, safe=False)
