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



# Create your views here.
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
