from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'Posts'  #With this variable we set all the Post.objects.all() to 'Posts' so we can loop in the html. <for post in Posts>
    ordering = ['-date']  #We order posts by field 'date' desc
    paginate_by: int = 9

    #the template name by convention is <app>/<model>_<viewtype>.html ------> blog/post_list.html


class UserPostListView(ListView):
    model = Post
    context_object_name = 'Posts'
    template_name: str = 'blog/post_user_list_post.html'    
    paginate_by: int = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(creator=user).order_by('-date')

class PostDetailView(DetailView):
    model = Post

    #The DetailView expects the context to be called OBJECT, so we have to change that in our template.

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image1', 'image2', 'image3']
    template_name = 'blog/post_create_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user #With this line we set up that the creator of the new post is the current login user. 
        return super().form_valid(form)    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image1', 'image2', 'image3']
    template_name = 'blog/post_update_form.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name= 'blog/post_delete_form.html'
    success_url = '/' #root page+
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        else:
            return False