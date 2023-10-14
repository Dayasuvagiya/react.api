from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer
from react_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ItemListView(generics.ListCreateAPIView):
    """View for listing and creating items."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
       user = self.request.user
       if user.is_anonymous:
        return Item.objects.none()  # Return an empty queryset for anonymous users
       return Item.objects.filter(owner=user)

    def perform_create(self, serializer):
      if self.request.user.is_anonymous:
        # Handle the case of an anonymous user, e.g., return an error response
        return Response({"detail": "Anonymous users cannot create items."}, status=400)



class ItemDetailedView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting an item."""
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(owner=user)