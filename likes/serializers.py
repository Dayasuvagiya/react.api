from rest_framework import serializers
from .models import likes


class LiskesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']
