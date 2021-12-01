from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home:category', kwargs={'name': self.name})

class Post(models.Model):
    title=models.CharField(max_length=255, verbose_name='Title')
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField()
    category=models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
     
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
        ordering=['pub_date']

    def __str__(self):
        return self.title

    def get_cat_list(self):
        return Post.objects.filter(category__name=self.name)
        k = self.category

    def get_absolute_url(self):
        return reverse('home:post', args=[self.pk])

class Recipe(Post):
    ingredients=models.TextField()
    method=Post.body
    serves=models.PositiveSmallIntegerField()
    time_to_make=models.PositiveSmallIntegerField()
    
