from django.forms import ModelForm
from .models import Book
from django.contrib.auth.models import User

 
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year_published', 'type', 'image']
 
        