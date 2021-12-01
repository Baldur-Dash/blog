from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category, Recipe 
# Create your views here.

class RecipeView(DetailView):
    model=Recipe
    template_name='home/recipe.html'
    def get_qeuryset(self):
        return Recipe.objects.all()

class WelcomeView(ListView):                                                            
    queryset = Post.objects.all()  #order_by('-pub_date')                                
    template_name = 'home/welcome.html' 

class PostView(DetailView):
    model = Post
    template_name = 'home/post.html'

class CategoryView(ListView):
    model=Post
    template_name='home/category.html'
    #The methods below were discovered at https://www.youtube.com/watch?v=uyTdSdOWHHk at 11:22, Credit to Emmanuel Okiche.

    def get_queryset(self): 
        self.category=get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context=super(CategoryView, self).get_context_data(**kwargs)
        context['category']=self.category
        return context

def cat_list(request):
    # category loops on navbar
    cat_list=Category.objects.filter()
    context = {"cat_list": cat_list,}
    return context
