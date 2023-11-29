from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def rooms(request):
    return render(request,"rooms.html")

def deluxe(request):
    return render(request,"deluxe.html")

def family(request):
    return render(request,"family.html")

def luxury(request):
    return render(request,"luxury.html")

def booking(request):
    return render(request,"booking.html")

def privacy(request):
    return render(request,"privacy.html")

def faq(request):
    return render(request,"faq.html")

def terms(request):
    return render(request,"terms.html")


def cancel(request):
    return render(request,"cancel.html")