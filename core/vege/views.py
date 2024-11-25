from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



# Create your views here.


@login_required(login_url="/login/")
def userDashboard(request):    
    return render(request,'USER_DASHBOARD.HTML')



def home(request):    
    return render(request,'INDEX2.html')
    


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user) 
            return redirect('/dashboard/') #after login which page to display

    return render(request, 'login.html')
    

def logout_page(request):
    logout(request)
    return redirect('/login/')






@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user': request.user})

@login_required
def edit_profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        profile_picture = request.FILES.get('profile_picture')
        
        user = request.user
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        if profile_picture:
            profile.profile_picture = profile_picture
        
        user.save()
        profile.save()
        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('profile')

    return render(request, 'edit_profile.html', {'user': request.user})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'password_form': password_form})











@login_required(login_url="/login/")
def helpSupport(request):    
    return render(request,'Help_Support.html')



def contactUs(request):
    if request.method =="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        msg=request.POST.get('msg')
        contact = Contact(firstname=firstname,lastname=lastname,email=email,phoneno=phoneno,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request, "Message Sent Sucessfully!")
    # return redirect('contact-us')
    return render(request, "contact-us.html")





@login_required(login_url="/login/")
def recipes(request): 
    if request.method == "POST":

        data = request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        category = data.get('category')
        serve = data.get('serve')
        cooktime = data.get('cooktime')
        taste = data.get('taste')
        ingredients = data.get('ingredients')
        instruction1 = data.get('instruction1')
        instruction2 = data.get('instruction2')
        instruction3 = data.get('instruction3')
        calories = data.get('calories') 
        carbohydrates = data.get('carbohydrates') 
        protein = data.get('protein') 
        fats = data.get('fats') 
        allergic_info = data.get('allergic_info') 


        Recipe.objects.create(
           recipe_name = recipe_name, 
           recipe_description = recipe_description,
           recipe_image = recipe_image,
           category = category,
           serve = serve,
           cooktime = cooktime,
           taste = taste,
           ingredients = ingredients,
           instruction1 = instruction1,
           instruction2 = instruction2,
           instruction3 = instruction3,
           calories = calories,
           carbohydrates = carbohydrates,
           protein = protein,
           fats = fats,
           allergic_info = allergic_info


        ) 
        # Add success message
        messages.info(request, "New Flavor Added to the Vault!")
        return redirect('/recipes/')
    
    # return render(request, 'recipes.html')
    # return redirect("/recipes/")    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'Recipe' : queryset}
    return render(request, 'recipes.html', context)



@login_required(login_url="/login/")
def viewRecipe(request):
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))
    context = {'recipes': queryset}
    return render(request, 'view_recipe.html', context)




def browseRecipe(request):
    if 'put' in request.GET:
        put =request.GET['put']
        browse =BrowseRecipe.objects.filter(recipe_name__icontains=put)
    else :
            browse= BrowseRecipe.objects.all()

    context ={
        'browse':browse
    }
    return render(request, "Browse.html",context)

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return HttpResponseRedirect(referer)
    return HttpResponseRedirect('/')






@login_required(login_url="/login/")
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id= id)
    queryset.delete()
    # Add success message
    messages.info(request, "Recipe Removed from the Vault!")
    return redirect('/recipes/')


@login_required(login_url="/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id= id)
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        category = data.get('category')
        serve = data.get('serve')
        cooktime = data.get('cooktime')
        taste = data.get('taste')
        ingredients = data.get('ingredients')
        instruction1 = data.get('instruction1')
        instruction2 = data.get('instruction2')
        instruction3 = data.get('instruction3')
        calories = data.get('calories') 
        carbohydrates = data.get('carbohydrates') 
        protein = data.get('protein') 
        fats = data.get('fats') 
        allergic_info = data.get('allergic_info') 



        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        queryset.category = category
        queryset.serve = serve
        queryset.cooktime = cooktime
        queryset.taste = taste
        queryset.ingredients = ingredients
        queryset.instruction1 = instruction1
        queryset.instruction2 = instruction2
        queryset.instruction3 = instruction3
        queryset.calories = calories
        queryset.carbohydrates = carbohydrates
        queryset.protein = protein
        queryset.fats = fats
        queryset.allergic_info = allergic_info
        if recipe_image:
            queryset.recipe_image = recipe_image 
        queryset.save()
        # Add success message
        messages.info(request, "New Twist Added to Your Recipe!")
        
        return redirect("/recipes/")    

    context = {'Recipe' : queryset}
    queryset = Recipe.objects.all()    
    return render(request, 'update_recipe.html', context)





def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username alreay taken')
            return redirect('/register/')
    
        user = User.objects.create(
            first_name = first_name ,
            last_name = last_name, 
            username = username,
            
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
            
    
        return redirect("/register/")    

    
    
    return render(request, 'register.html')



def feedback_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        feedback_type = request.POST.get('feedback_type')
        details = request.POST.get('details')
        rating = request.POST.get('rating')
        recommend = request.POST.get('recommend')
        email = request.POST.get('email')
        additional_comments = request.POST.get('additional_comments')
        
        # Create a new Feedback instance
        Feedback.objects.create(
            subject=subject,
            feedback_type=feedback_type,
            details=details,
            rating=rating,
            recommend=recommend == 'true',  # Convert string to boolean
            email=email,
            additional_comments=additional_comments
        )
        
        # Use Django's messages framework to display a success message
        messages.info(request, "Thank you for your feedback!")
        
        # Redirect to the same page to show the message
        return redirect('feedback')
    
    return render(request, 'feedback.html')

@login_required(login_url="/login/")
def meal_planner(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        day = request.POST.get('day')

        if recipe_name and day:
            # Create or get existing Recipe
            recipe, created = Recipe.objects.get_or_create(recipe_name=recipe_name)

            # Create or get existing MealPlan for the logged-in user
            meal_plan, created = MealPlanner.objects.get_or_create(
                user=request.user, day=day, recipe=recipe
            )

            if created:
                messages.success(request, f'Recipe "{recipe_name}" added to "{day}" successfully!')
            else:
                messages.info(request, f'Recipe "{recipe_name}" is already planned for "{day}".')

            # Redirect to avoid re-posting on refresh
            return redirect('meal_planner')

    # Fetch meal plans for the logged-in user
    meal_plans = MealPlanner.objects.filter(user=request.user)
    return render(request, 'meal_planner.html', {'meal_plans': meal_plans})

@login_required(login_url="/login/")
def meal_plan_view(request):
    # Fetch meal plans only for the logged-in user
    meal_plans = MealPlanner.objects.filter(user=request.user)
    return render(request, 'meal_plan.html', {'meal_plans': meal_plans})



@login_required(login_url="/login/")
def grocery_list_view(request):
    if request.method == 'POST':
        item_name = request.POST.get('Item_name')  # Fixing capitalization to snake_case
        quantity = request.POST.get('Quantity')

        if item_name and quantity:
            # Create a grocery item for the logged-in user
            GroceryItems.objects.create(
                user=request.user,
                item_name=item_name,
                quantity=quantity
            )
            messages.success(request, "Grocery item added successfully!")
        else:
            messages.error(request, "Please provide valid item details.")

        return redirect('grocery_list')

    # Fetch grocery items for the current user
    grocery_items = GroceryItems.objects.filter(user=request.user)
    return render(request, 'grocery_list.html', {'grocery_items': grocery_items})

@login_required(login_url="/login/")
def added_grocery_list(request):
    # Fetch only grocery items for the logged-in user
    grocery_items = GroceryItems.objects.filter(user=request.user)
    return render(request, 'grocery_list_view.html', {'grocery_items': grocery_items})



@login_required(login_url="/login/")
def add_cooking_schedule(request):
    if request.method == 'POST':
        meal_plan_id = request.POST.get('meal_plan')
        scheduled_time = request.POST.get('scheduled_time')
        
        if meal_plan_id and scheduled_time:
            meal_plan = MealPlanner.objects.get(id=meal_plan_id)
            scheduled_time = parse_datetime(scheduled_time)
            
            # Create a cooking schedule for the logged-in user
            CookingSchedules.objects.create(
                user=request.user,  # Associate with logged-in user
                meal_plan=meal_plan,
                scheduled_time=scheduled_time
            )
            messages.info(request, "Scheduled successfully!")

            return redirect('cooking_schedule')
    
    meal_plans = MealPlanner.objects.filter(user=request.user)  # Filter meal plans for the logged-in user
    return render(request, 'cooking_schedule.html', {'meal_plans': meal_plans})

@login_required(login_url="/login/")
def cooking_schedule_view(request):
    # Fetch only cooking schedules for the logged-in user
    cooking_schedules = CookingSchedules.objects.filter(user=request.user)
    return render(request, 'cooking_schedule_view.html', {'cooking_schedules': cooking_schedules})






# Delete Meal Plan
@login_required(login_url="/login/")
def delete_meal_plan(request, id):
    meal_plan = get_object_or_404(MealPlanner, id=id, user=request.user)
    meal_plan.delete()
    messages.success(request, "Meal Plan deleted successfully!")
    return redirect('meal_plan')

# Delete Grocery Item
@login_required(login_url="/login/")
def delete_grocery_item(request, id):
    grocery_item = get_object_or_404(GroceryItems, id=id)
    grocery_item.delete()
    messages.success(request, "Grocery Item deleted successfully!")
    return redirect('view_grocery')

# Delete Cooking Schedule
@login_required(login_url="/login/")
def delete_cooking_schedule(request, id):
    cooking_schedule = get_object_or_404(CookingSchedules, id=id, user=request.user)
    cooking_schedule.delete()
    messages.success(request, "Cooking Schedule deleted successfully!")
    return redirect('view_cooking_schedule')











@login_required
def ecom_home(request):
    query = request.GET.get('q', '')
    if query:
        ingredients = Ingredient.objects.filter(Q(name__icontains=query) | Q(description__icontains=query), stock__gt=0)
    else:
        ingredients = Ingredient.objects.filter(stock__gt=0)
    return render(request, 'ecom_home.html', {'ingredients': ingredients, 'query': query})

@login_required
def add_to_cart(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, ingredient=ingredient)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    # Add a success message
    messages.success(request, f"{ingredient.name} has been added to your cart!")

    # Redirect back to the referring page or home
    return redirect(request.META.get('HTTP_REFERER', 'ecom_home'))

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')

@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_view')

@login_required
def remove_from_cart(request, ingredient_id):
    cart = Cart.objects.get(user=request.user)
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    # Find the cart item to remove
    cart_item = CartItem.objects.filter(cart=cart, ingredient=ingredient).first()
    
    if cart_item:
        cart_item.delete()  # Remove the item from the cart
    
    return redirect('cart_view')

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        order = Order.objects.create(
            user=request.user,
            cart=cart,
            address=address,
            is_cash_on_delivery=True if payment_method == 'COD' else False
        )

        # Handle cash on delivery only for now
        if payment_method == 'ONLINE':
            return render(request, 'payment_coming_soon.html')

        # Empty the cart after ordering
        cart.cartitem_set.all().delete()

        return redirect('order_confirmation', order_id=order.id)
    
    return render(request, 'checkout.html', {'cart': cart})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Debugging print statement to check if cart total is working
    # print("Total amount for order:", order.cart.get_total())  # This should print in the console

    return render(request, 'order_confirmation.html', {'order': order})