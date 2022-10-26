from django.http import HttpResponse
from django.template import loader
 
def books(request):
   template = loader.get_template('books.html')
   context = {
       'book_list': ['Harry Potter','Lord of the Rings','Hobbit'],
   }
   return HttpResponse(template.render(context, request))
