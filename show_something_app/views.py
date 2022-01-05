# Each view is responsible for doing one of two things: returning an HttpResponse object to the contents of the requested page, or raising an exception such as Http404. The rest is up to you.

# Here we just use the render method imported so we can render a html-page
from django.shortcuts import render

# Create your views here.
def say_hello(request):
   return render(request, 'hello.html', {'name':'Gustaf'})
