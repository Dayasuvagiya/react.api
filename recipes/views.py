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
       if user.is_anonymous:
        return Recipe.objects.none()  # Return an empty queryset for anonymous users
       return Recipe.objects.filter(owner=user)

    def perform_create(self, serializer):
      if self.request.user.is_anonymous:
        # Handle the case of an anonymous user, e.g., return an error response
        return Response({"detail": "Anonymous users cannot create items."}, status=400)

    # Proceed with saving the owner as the current user
      serializer.save(owner=self.request.user)

class RecipeDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting an recipe."""
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.filter(owner=user)