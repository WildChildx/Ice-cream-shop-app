from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import date, datetime
from django.contrib import messages

def index(request):
    context = {
        'variable1':"Shree is great",
        'variable2':"Harry is great"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        contact = Contact(name=name,email=email,number=number,date=datetime.today())
        contact.save()
        messages.success(request, 'Your credentials are sent successfully')
    return render(request,'contact.html')
