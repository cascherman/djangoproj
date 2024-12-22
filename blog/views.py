from django.shortcuts import render




# Create your views here.

posts = [
    {
        'author': 'Chris',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': "Dec 17, 2024",
    },
    {
        'author': 'Fred',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': "Dec 18, 2024",
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})