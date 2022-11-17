from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.basicbooks),
    path('books/<pk>',views.book),
]

