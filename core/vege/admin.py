from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Recipe),
admin.site.register(BrowseRecipe),
admin.site.register(Contact),
admin.site.register(Feedback),
@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('day', 'recipe')
    search_fields = ('day', 'recipe__recipe_name')
    list_filter = ('day', 'recipe')

@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('Item_name', 'Quantity')
    search_fields = ('Item_name',)

@admin.register(CookingSchedule)
class CookingScheduleAdmin(admin.ModelAdmin):
    list_display = ('meal_plan', 'scheduled_time')
    search_fields = ('meal_plan__day',)
    list_filter = ('scheduled_time',)


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