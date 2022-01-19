from django import http
from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    #context = {
       # "variable":"   #this is sent"
    #}
    
    return render(request,'index.html')

def about(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        about = Contact(name= name ,email= email,phone=phone,desc=desc,date=datetime.today())
        about.save()
        messages.success(request, 'Well done! Your form has been succesfully submitted')

    

    #return HttpResponse("this is aboutpage")
    return render(request,'about.html')
def contact(request):
     
    #return HttpResponse("this is about_contact")
    return render(request,'contact.html')
def services(request):
    #return HttpResponse("this is about_services")
    return render(request,'services.html')
def price(request):
    return render(request,'price.html')
    #return HttpResponse("this is about_services")
    