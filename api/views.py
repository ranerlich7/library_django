from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def example(request):
    usage = ['GET \ usage', 
    'GET \books book list',
    'GET \books\[id] single book']
    return Response(usage)

@api_view(['GET'])
def books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
