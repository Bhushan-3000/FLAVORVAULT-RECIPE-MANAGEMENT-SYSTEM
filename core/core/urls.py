"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', home),
    path('dashboard/', userDashboard, name="userDashboard"),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('change-password/', change_password_view, name='change_password'),
    path('browse_recipes/', browseRecipe),
    path('recipes/', recipes, name ="recipes"),
    path('view_recipe/', viewRecipe, name='viewRecipe'),
    path('Contact_Us/', contactUs),
    path('help_support/', helpSupport),
    path('delete_recipe/<id>/',delete_recipe , name ="delete_recipe"),
    path('update_recipe/<id>/',update_recipe , name ="update_recipe"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('register/', register, name="register"),
    path('admin/', admin.site.urls),
    path('feedback/', feedback_view, name='feedback'),
    path('meal_planner/', meal_planner, name='meal_planner'),
    path('meal_plan/', meal_plan_view, name='meal_plan'),
    path('grocery_list/', grocery_list_view, name='grocery_list'),
    path('view_grocery/', added_grocery_list, name='view_grocery'),
    path('cooking_schedule/', add_cooking_schedule, name='cooking_schedule'),
    path('view_cooking_schedule/', cooking_schedule_view, name='view_cooking_schedule'),
    path('ecom/', ecom_home, name='ecom_home'),
    path('ecom/add_to_cart/<int:ingredient_id>/', add_to_cart, name='add_to_cart'),
    path('ecom/cart/', cart_view, name='cart_view'),  # Ensure this line exists
    path('ecom/increase_quantity/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('ecom/decrease_quantity/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('ecom/remove_from_cart/<int:ingredient_id>/', remove_from_cart, name='remove_from_cart'),
    path('ecom/checkout/', checkout, name='checkout'),
    path('ecom/order_confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('meal_plan/delete/<int:id>/', delete_meal_plan, name='delete_meal_plan'),
    path('grocery_item/delete/<int:id>/', delete_grocery_item, name='delete_grocery_item'),
    path('cooking_schedule/delete/<int:id>/', delete_cooking_schedule, name='delete_cooking_schedule'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()  


admin.site.site_header = "FLAVORVAULT ADMINISTRATION"
admin.site.site_title = "FlavorVault Admin Postal"
admin.site.index_title = "Welcome to FlavorVault Admin Portal"