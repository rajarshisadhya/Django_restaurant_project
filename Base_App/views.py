from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import *

# Create your views here.
def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, "home.html", {"items": items, "list": list, "review": review}) 

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, "menu.html", {"items": items, "list": list}) 

def BookTableView(request):
    if request.method == "POST":
        name = request.POST.get("user_name")
        email = request.POST.get("user_email")
        phone_number = request.POST.get("phone_number")
        booking_date = request.POST.get("booking_data")
        total_person = request.POST.get("total_person")

        if name != "" and email != "" and phone_number != "" and booking_date != "" and total_person != "":


            booking = BookTable(Name=name, Email=email, Phone_number=phone_number, Booking_date=booking_date, Total_person=total_person)
            booking.save()
    return render(request, "book_table.html")  

def AboutView(request):
    return render(request, "about.html")    

def FeebackView(request):
    return render(request, "feedback.html")

def LoginView(request):
    return render(request, "login.html")

def SignUpView(request):
    pass