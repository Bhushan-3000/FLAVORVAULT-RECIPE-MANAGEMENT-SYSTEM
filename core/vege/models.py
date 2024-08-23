from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")


    
# class Contact(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     full_name = models.CharField(max_length=100)
#     contact_number = models.CharField(max_length=100)
#     email_add = models.EmailField(max_length=100)
#     message_box = models.TextField()
