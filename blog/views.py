from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'Posts'  #With this variable we set all the Post.objects.all() to 'Posts' so we can loop in the html. <for post in Posts>
    ordering = ['-date']  #We order posts by field 'date' desc

    #the template name by convention is <app>/<model>_<viewtype>.html ------> blog/post_list.html


class PostDetailView(DetailView):
    model = Post

    #The DetailView expects the context to be called OBJECT, so we have to change that in our template.

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user #With this line we set up that the creator of the new post is the current login user. 
        return super().form_valid(form)    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
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
    success_url = '/' #root page
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        else:
            return False