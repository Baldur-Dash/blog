from django.urls import path
from . import views
from .views import WelcomeView, PostView, CategoryView, RecipeView

app_name = 'home'

urlpatterns = [
        path('', WelcomeView.as_view(), name='welcome'),
        path('post/<int:pk>', PostView.as_view(), name='post'),
        path('category/<int:pk>', CategoryView.as_view(), name='category'),
        path('recipe', RecipeView.as_view(), name='recipe'),
        #path('', .as_view(), name=''),
        ]
