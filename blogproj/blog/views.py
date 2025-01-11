from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


posts = [
{    "author":"John Smith",
    "title":"Blog post 1",
     "content":"This is my 1st blog",
     "date_posted":"14th August 2012"
},
{
    "author":"Will Smith",
    "title":"Blog post 2",
    "content":"This is my 2nd blog",
    "date_posted":"18th August 2012"  
}
]


def home(request):    
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
  

def about(request):
    return render(request,'blog/about.html', {'title':'About Page '})
