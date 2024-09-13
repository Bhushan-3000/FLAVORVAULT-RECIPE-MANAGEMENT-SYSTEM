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