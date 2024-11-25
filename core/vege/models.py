from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'









class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    category = models.CharField(max_length=100, null=True)
    serve = models.CharField(max_length=100, null=True)
    cooktime = models.CharField(max_length=100, null=True)
    taste = models.CharField(max_length=100, null=True)
    ingredients = models.CharField(max_length=1000, null=True)
    instruction1 = models.CharField(max_length=1000, null=True)
    instruction2 = models.CharField(max_length=1000, null=True)
    instruction3 = models.CharField(max_length=1000, null=True)
    calories = models.CharField(max_length=200, null=True)
    carbohydrates = models.CharField(max_length=200, null=True)
    protein = models.CharField(max_length=200, null=True)
    fats = models.CharField(max_length=200, null=True)
    allergic_info = models.CharField(max_length=1000, null=True)
    
    def __str__(self) -> str:
        return self.recipe_name




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
    description = models.CharField(max_length=800)
    category = models.CharField(max_length=100)
    serve = models.CharField(max_length=100, null=True)
    cooktime = models.CharField(max_length=100, null=True)
    taste = models.CharField(max_length=100, null=True)
    ingredients = models.CharField(max_length=1000)
    instruction1 = models.CharField(max_length=1000, null=True)
    instruction2 = models.CharField(max_length=1000, null=True)
    instruction3 = models.CharField(max_length=1000, null=True)
    calories = models.CharField(max_length=200, null=True)
    carbohydrates = models.CharField(max_length=200, null=True)
    protein = models.CharField(max_length=200, null=True)
    fats = models.CharField(max_length=200, null=True)
    allergic_info = models.CharField(max_length=1000, null=True)
    
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
    

class MealPlan(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day}: {self.recipe.recipe_name}"


# new model mealplan 

class MealPlanner(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate with a user
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s {self.day}: {self.recipe.recipe_name}"




class GroceryItem(models.Model):
    Item_name = models.CharField(max_length=255)
    Quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Quantity} of {self.Item_name}"



# new grocery list 
class GroceryItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate each item with a user
    item_name = models.CharField(max_length=255)  # Follow Python naming conventions (snake_case)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.item_name}"

class CookingSchedule(models.Model):
    meal_plan = models.OneToOneField(MealPlan, on_delete=models.CASCADE)
    scheduled_time = models.TimeField()

    def __str__(self):
        return f"{self.meal_plan} at {self.scheduled_time}"
    


# new cooking schedule 

class CookingSchedules(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate schedule with a user
    meal_plan = models.ForeignKey(MealPlanner, on_delete=models.CASCADE, null=True)  # Link to the specific meal plan
    scheduled_time = models.DateTimeField()  # The time when the recipe will be cooked

    def __str__(self):
        return f"{self.meal_plan.recipe.recipe_name} scheduled for {self.scheduled_time} by {self.user.username}"





class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='ingredient_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through='CartItem')

    def get_total(self):
        # Calculate the total amount by summing up the totals of all CartItems
        return sum(item.get_total() for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total(self):
        return self.quantity * self.ingredient.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    is_cash_on_delivery = models.BooleanField(default=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"