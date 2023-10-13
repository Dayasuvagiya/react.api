from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the Recipe model."""
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'content', 'created_at', 'updated_at']


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detailed Recipe model."""
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'content', 'created_at', 'updated_at']
