from django.contrib.auth import authenticate, login,  logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from itertools import chain
from django.contrib import messages
import itertools
from .models import *
from django.db.models import Q
from django.db.models import Count
from django.utils import timezone
from django.db.models import Q, Count
import datetime
from django.db.models import F
from django.contrib.auth.hashers import make_password
from django.db.models import Avg
from app1.models import company


import datetime

from datetime import datetime, timedelta
import requests


from decimal import Decimal


def index(request):
    cat = categories.objects.all()  # Add parentheses to the .all() method
    return render(request, "index.html", {"cat": cat})



def companyprofile(request,id,pk):
    comp=company.objects.filter(category_name__category_name=id,id=pk)
    return render(request,"companyprofile.html",{"comp":comp} )


def about(request):
    return render(request,"about-us.html")


def add_category(request):
    return render(request,"add_category.html")



def adding_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        
        # Handle image upload
        image = request.FILES.get('image')
        
        new_category = categories(category_name=category_name, image=image)
        new_category.save()
        
        return redirect('add_category')  # Redirect to the category list page after adding a new category
    
   


from django.shortcuts import render, redirect
from .models import company

def add_company(request):

    cat=categories.objects.all()

    return render(request, 'add_company.html',{"cat":cat})


def adding_company(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        company_n = request.POST.get('company_n')
        description = request.POST.get('description')
        address = request.POST.get('address')
        company_image = request.FILES.get('company_image')
        mobile = request.POST.get('mobile')
        alt_mobile = request.POST.get('alt_mobile')
        email = request.POST.get('email')
        web_link = request.POST.get('web_link')
        fb_link = request.POST.get('fb_link')
        insta_link = request.POST.get('insta_link')
        linkdin_link = request.POST.get('linkdin_link')
        twit_link = request.POST.get('twit_link')
        whatsapp_link = request.POST.get('whatsapp_link')
        location_link = request.POST.get('location_link')
        
        service_1 = request.POST.get('service_1')
        service_2 = request.POST.get('service_2')
        service_3 = request.POST.get('service_3')
        service_4 = request.POST.get('service_4')
        service_5 = request.POST.get('service_5')
        service_6 = request.POST.get('service_6')
        service_7 = request.POST.get('service_7')
        service_8 = request.POST.get('service_8')
        image = request.FILES.get('image')
        image_2 = request.FILES.get('image_2')
        image_3 = request.FILES.get('image_3')
        image_4 = request.FILES.get('image_4')
        image_5 = request.FILES.get('image_5')
        image_6 = request.FILES.get('image_6')

       

        new_company = company(
          
            company_n=company_n,
            description=description,
            address=address,
            company_image=company_image,
            mobile=mobile,
            alt_mobile=alt_mobile,
            email=email,
            fb_link=fb_link,
            insta_link=insta_link,
            linkdin_link=linkdin_link,
            twit_link=twit_link,
            whatsapp_link=whatsapp_link,
            location_link=location_link,
            service_1=service_1,
            service_2=service_2,
            service_3=service_3,
            service_4=service_4,
            service_5=service_5,
            service_6=service_6,
            service_7=service_7,
            service_8=service_8,
            image=image,
            image_2=image_2,
            image_3=image_3,
            image_4=image_4,
            image_5=image_5,
            image_6=image_6,
           
            web_link=web_link
        )
        if category_name:
            try:
                intr_instance = categories.objects.get(id=category_name)
                new_company.category_name = intr_instance
               
            except categories.DoesNotExist:
                pass     
        new_company.save()

        return redirect('add_company')  # Redirect to the company list view after successful submission

  


def add_category(request):
    return render(request,"add_category.html")



def adminpanel(request):
    return render(request,"adminpanel.html")


def delete(request,pk):
    com=company.objects.get(id=pk)
    com.delete()
    return redirect("all_companies")

def signup(request):

    return render(request, 'signup.html', {'error': 'All fields are required'})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if a user with the same username already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already taken. Please choose another username."
            return render(request, "signup.html", {"error_message": error_message})

        # Hash the password securely
        hashed_password = make_password(password)

        # Create and save the user
        user = User.objects.create(username=username, password=hashed_password)

        return redirect("signup")  # Redirect to the signup page after successful registration

    return render(request, "signup.html")  #





def login_v(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Debugging: Print the values to check
      
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            
            # Debugging: Print user information
            print("Authenticated User:", user)
            
            # Redirect staff users to admin panel
            return redirect('index')
        else:
            error_message = "Invalid username and/or password."
            return render(request, "login.html", {"error_message": error_message})
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))    
    


def blog(request):
    return render(request,"blog-list-4.html")

def all_companies(request):
    companies = company.objects.all()
    print(companies)
    return render(request, "all_companies.html", {'companies': companies})



def category(request,id):
    cat = categories.objects.all()
    comp=company.objects.filter(category_name__category_name=id)
    return render(request,"category.html",{"comp":comp,"cat":cat})

def all_categories(request):
    cat = categories.objects.all()
    return render(request,"all_categories.html" , {"cat": cat})