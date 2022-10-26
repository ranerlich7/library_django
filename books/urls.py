from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
   url(r'^/', views.books, name="books"),
   url('add/', views.add_book, name="add"),
   url('add_book_action/', views.add_book_action, name="add_book_action"),
   url('search/', views.find_book, name="search"),
   url('delete/', views.delete_book, name="delete"),
   
]
