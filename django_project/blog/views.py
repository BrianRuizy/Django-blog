from django.shortcuts import render
from django.http import HttpResponse

#dummy data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Aug 27, 2018',
    },
    {
    
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Aug 28, 2018',
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

