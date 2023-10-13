from django.urls import path
from .views import RecipeListView, RecipeDetailedView


urlpatterns = [
    path('recipes/', RecipeListView.as_view()),
    path('recipes/<int:pk>/', RecipeDetailedView.as_view())
]