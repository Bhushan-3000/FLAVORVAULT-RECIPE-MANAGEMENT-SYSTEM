from urllib import request
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_datetime



# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('recipes')  
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')  # Redirect to the login page or home








def home(request):    
    return render(request,'INDEX2.html')
    # if request.method == "POST":

    #     data = request.POST
        
    #     full_name = data.get('full_name')
    #     contact_number = data.get('contact_number')
    #     email_add = data.get('email_add')
    #     message_box = data.get('message_box')
        
    #     print(full_name)
    #     print(contact_number)
    #     print(email_add)
    #     print(message_box)

    #     Contact.objects.create(
    #        full_name = full_name, 
    #        contact_number = contact_number,
    #        email_add = email_add,
    #        message_box = message_box,

    #     )
    #     return redirect("/home/")    
    # queryset = Contact.objects.all()




# def browse_recipe(request):    
#     return render(request,'browse_recipes.html')






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
        
        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

        Recipe.objects.create(
           recipe_name = recipe_name, 
           recipe_description = recipe_description,
           recipe_image = recipe_image,
        )
        return redirect("/recipes/")    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'Recipe' : queryset}
    return render(request, 'recipes.html', context)





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
    return redirect('/recipes/')


@login_required(login_url="/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id= id)
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        if recipe_image:
            queryset.recipe_image = recipe_image 
        queryset.save()
        return redirect("/recipes/")    

    context = {'Recipe' : queryset}
    queryset = Recipe.objects.all()    
    return render(request, 'update_recipe.html', context)


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
            return redirect('/recipes/')

    return render(request, 'login.html')
    

def logout_page(request):
    logout(request)
    return redirect('/login/')




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

            # Create or get existing MealPlan
            meal_plan, created = MealPlan.objects.get_or_create(day=day, recipe=recipe)

            if created:
                messages.success(request, f'Recipe "{recipe_name}" added to "{day}" successfully!')
            else:
                messages.info(request, f'Recipe "{recipe_name}" is already planned for "{day}".')

            # Redirect to avoid re-posting on refresh
            return redirect('meal_planner')
    
    # Fetch all meal plans, grocery items, and cooking schedules to display
    meal_plans = MealPlan.objects.all()
    grocery_items = GroceryItem.objects.all()
    cooking_schedules = CookingSchedule.objects.all()

    return render(request, 'meal_planner.html', {
        'meal_plans': meal_plans,
        'grocery_items': grocery_items,
        'cooking_schedules': cooking_schedules
    })


def meal_plan_view(request):
    meal_plans = MealPlan.objects.all()
    return render(request, 'meal_plan.html', {'meal_plans': meal_plans})




@login_required(login_url="/login/")
def grocery_list_view(request):
    if request.method == 'POST':
        Item_name = request.POST.get('Item_name')
        Quantity = request.POST.get('Quantity')

        GroceryItem.objects.create(
            Item_name=Item_name,
            Quantity=Quantity
            )
        
        messages.info(request, "Grocery Item Added Successfully!")
        
        return redirect('grocery_list')
    
    return render(request, 'grocery_list.html')



def added_grocery_list(request):
    grocery_items = GroceryItem.objects.all()
    return render(request, 'grocery_list_view.html', {'grocery_items': grocery_items})



@login_required(login_url="/login/")
def add_cooking_schedule(request):
    if request.method == 'POST':
        meal_plan_id = request.POST.get('meal_plan')
        scheduled_time = request.POST.get('scheduled_time')
        
        if meal_plan_id and scheduled_time:
            meal_plan = MealPlan.objects.get(id=meal_plan_id)
            scheduled_time = parse_datetime(scheduled_time)
            
            CookingSchedule.objects.create(
                meal_plan=meal_plan,
                scheduled_time=scheduled_time
            )
            messages.info(request, "Scheduled Successfully!")

            return redirect('cooking_schedule')
    
    meal_plans = MealPlan.objects.all()
    return render(request, 'cooking_schedule.html', {'meal_plans': meal_plans})

def cooking_schedule_view(request):
    cooking_schedules = CookingSchedule.objects.all()  # Filter as needed
    return render(request, 'cooking_schedule_view.html', {'cooking_schedules': cooking_schedules})







# def cooking_schedule_view(request):
#     cooking_schedules = CookingSchedule.objects.all()
#     return render(request, 'cooking_schedule.html', {'cooking_schedules': cooking_schedules})

