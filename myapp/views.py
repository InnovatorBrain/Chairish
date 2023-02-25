from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Checkout


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def cart(request):
    return render(request, 'cart.html')



def checkout(request):
    # Post Request >> form content >> Thanks
    if request.method == "POST":
        form = Checkout(request.POST)
        if form.is_valid():
            # Save form data to database using Checkout model
            checkout = Checkout(
                country=form.cleaned_data["country"],
                fname=form.cleaned_data["fname"],
                lname=form.cleaned_data["lname"],
                companyname=form.cleaned_data.get("companyname", None),
                address=form.cleaned_data["address"],
                state_or_province=form.cleaned_data["state_or_province"],
                postal_code=form.cleaned_data["postal_code"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                order_notes=form.cleaned_data.get("order_notes", None),
                coupon_code=form.cleaned_data.get("coupon_code", None)
            )
            checkout.save()
            return redirect(reverse("myapp:checkout"))
    # Else render form
    else:
        form = Checkout()
    return render(request, "checkout.html", context={"form": form})

def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def shop(request):
    return render(request, 'shop.html')


def thankyou(request):
    return render(request, 'thankyou.html')

# def handler404(request, exception):              >>> for error msg code having error
#     return render(request, '404.html', status=404)
