from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
   url('', views.books, name="books"),
   url('add/', views.add_book, name="add"),
   url('search/', views.find_book, name="search"),
   url('delete/', views.delete_book, name="delete"),
   
]
