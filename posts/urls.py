from django.urls import path
from posts import views

# Post URLs
urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view())
]