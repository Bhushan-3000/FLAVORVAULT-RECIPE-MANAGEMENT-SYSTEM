from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Recipe),
admin.site.register(BrowseRecipe),
admin.site.register(Contact),
admin.site.register(Feedback),
@admin.register(MealPlanner)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('day', 'recipe')
    search_fields = ('day', 'recipe__recipe_name')
    list_filter = ('day', 'recipe')

@admin.register(GroceryItems)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_name', 'quantity')
    list_filter = ('user',)
    search_fields = ('item_name', 'user__username')
    readonly_fields = ('user',)  # Optional: Make 'user' read-only

@admin.register(CookingSchedules)
class CookingScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'meal_plan', 'scheduled_time')  # Display the user, meal plan, and scheduled time
    search_fields = ('meal_plan__day', 'meal_plan__recipe__recipe_name', 'user__username')  # Search by day, recipe, and user
    list_filter = ('user', 'scheduled_time')  # Filter by user and scheduled time

# Admin for Ingredient model
class IngredientAdmin(admin.ModelAdmin): 
    list_display = ['name', 'price', 'stock', 'description', 'image']
    search_fields = ['name', 'description']
    list_filter = ['stock']
    ordering = ['name']

# Admin for Cart model
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_total']

# Custom method to display CartItems in OrderAdmin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_cash_on_delivery', 'is_paid', 'get_total']
    list_filter = ['is_cash_on_delivery', 'is_paid']
    search_fields = ['user__username', 'address']

    # Display cart items in the order detail page
    def get_cart_items(self, obj):
        cart_items = obj.cart.cartitem_set.all()  # Fetch cart items from the related cart
        return "\n".join([f"{item.ingredient.name} (x{item.quantity})" for item in cart_items])

    get_cart_items.short_description = 'Ordered Items'

    # Display total amount
    def get_total(self, obj):
        return obj.cart.get_total()

    get_total.short_description = 'Total Amount'

    # Customizing the order detail view to show the cart items
    fieldsets = (
        (None, {
            'fields': ('user', 'address', 'is_cash_on_delivery', 'is_paid', 'get_total', 'get_cart_items')
        }),
    )

    readonly_fields = ('get_total', 'get_cart_items')  # Make cart items and total read-only

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)