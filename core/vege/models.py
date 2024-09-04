from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")


class BrowseRecipe(models.Model):
    recipe_name= models.CharField(max_length=200)
    img = models.ImageField(upload_to="browseRecipes")
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    ingredients = models.CharField(max_length=800)
    instructions = models.CharField(max_length=200)
    nutritional_info = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.recipe_name

    