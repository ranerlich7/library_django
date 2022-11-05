from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'books'

urlpatterns = [
   url(r'^/', login_required(views.books, login_url='elogin'), name="books"),
   url('add/', views.add_book, name="add"),
   url('add_book_action/', views.add_book_action, name="add_book_action"),
   url('search/', views.find_book, name="search"),
   url('delete/', views.delete_book, name="delete"),
   
]
