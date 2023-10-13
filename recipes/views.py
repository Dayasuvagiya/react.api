from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer, RecipeDetailSerializer
from react_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class RecipeListView(generics.ListCreateAPIView):
    """View for listing and creating Recipe."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Save the owner of the recipe as the current user."""
        serializer.save(owner=self.request.user)


class RecipeDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting an recipe."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.filter(owner=user)