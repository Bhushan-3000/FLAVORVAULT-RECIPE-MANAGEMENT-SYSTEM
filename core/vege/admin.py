from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Recipe),
admin.site.register(BrowseRecipe),
admin.site.register(Contact),
admin.site.register(Feedback)