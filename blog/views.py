from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'Posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)