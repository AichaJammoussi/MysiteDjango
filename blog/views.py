from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.forms import PostForm
from .models import Post

class ListePosts(ListView):
    model = Post
    template_name = 'mag/liste_Posts.html'
    context_object_name = 'Post'
class DetailPost(DetailView):
    model = Post
    template_name = 'mag/detail_Post.html'
    context_object_name = 'Post'
class CreerPost(CreateView):
    model = Post
    template_name = 'mag/creer_Post.html'
    form_class = PostForm 
    success_url = reverse_lazy('liste_Posts') 

class ModifierPost(UpdateView):
    model = Post
    template_name = 'mag/modifier_Post.html'
    form_class = PostForm 
    success_url = reverse_lazy('liste_Posts') 
    
class SupprimerPost(DeleteView):
    model = Post
    template_name = 'mag/supprimer_Post.html'
    success_url = reverse_lazy('liste_Posts') 

