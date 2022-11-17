from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def book(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book,many=False)
    return Response(serializer.data)

