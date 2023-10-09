from rest_framework import generics, permissions
from react_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LiskesSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LiskesSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LiskesSerializer
    queryset = Like.objects.all()