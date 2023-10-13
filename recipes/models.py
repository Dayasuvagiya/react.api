from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    """
    Model for posting Recipes.
    Assigns fields and method for model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.quantity}"
    
    class Meta:
        ordering = ['-created_at']