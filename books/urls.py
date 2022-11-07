from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'books'

urlpatterns = [
   path('', login_required(views.books, login_url='elogin'), name="books"),
   path('add/', views.add_book, name="add"),
   path('add_book_action/', views.add_book_action, name="add_book_action"),
   path('search/', views.find_book, name="search"),
   path('delete/', views.delete_book, name="delete"),
   path('book_detail/<pk>/', views.book_detail, name="book_detail"),
   path('edit/<pk>/', views.edit, name="edit"),
   
]
