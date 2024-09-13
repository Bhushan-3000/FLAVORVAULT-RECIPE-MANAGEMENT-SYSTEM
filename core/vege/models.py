from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")



class Contact(models.Model):
    firstname= models.CharField(max_length=120)
    lastname= models.CharField(max_length=120)
    email= models.CharField(max_length=120)
    phoneno = models.CharField(max_length=15)
    msg = models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.firstname






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

    
    
class Feedback(models.Model):
    FEEDBACK_TYPE_CHOICES = [
        ('suggestion', 'Suggestion'),
        ('issue', 'Problem/Issue'),
        ('praise', 'Praise/Compliment'),
        ('general', 'General Question'),
    ]

    subject = models.CharField(max_length=100)
    feedback_type = models.CharField(max_length=10, choices=FEEDBACK_TYPE_CHOICES)
    details = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5
    recommend = models.BooleanField()
    email = models.EmailField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject} - {self.feedback_type}"