from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")


class BrowseRecipe(models.Model):
    recipe_name= models.CharField(max_length=500)
    img = models.ImageField(upload_to="browseRecipes")
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    serve = models.CharField(max_length=100, default='No info')
    cooktime = models.CharField(max_length=100, default='No info')
    taste = models.CharField(max_length=100, default='No info')
    ingredients = models.CharField(max_length=1000)
    instruction1 = models.CharField(max_length=1000, default='No info')
    instruction2 = models.CharField(max_length=1000, default='No info')
    instruction3 = models.CharField(max_length=1000, default='No info')
    calories = models.CharField(max_length=200, default='No info')
    carbohydrates = models.CharField(max_length=200, default='No info')
    protein = models.CharField(max_length=200, default='No info')
    fats = models.CharField(max_length=200, default='No info')
    allergic_info = models.CharField(max_length=1000, default='No info')
    
    def __str__(self) -> str:
        return self.recipe_name

    