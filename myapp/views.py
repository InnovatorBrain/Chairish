from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello, world!")

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def shop(request):
    return render(request, 'shop.html')

def thankyou(request):
    return render(request, 'thankyou.html')

