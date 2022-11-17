from django.urls import path
from . import views

urlpatterns = [
    path('',views.example),
    path('book/',views.books),
    path('book/<pk>/',views.book)
]