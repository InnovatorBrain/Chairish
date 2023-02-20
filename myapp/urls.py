from django.urls import path
from . import views
from django.urls import path
from . import views
# from .views import handler404           >>> for error msg code having error 
# handler404 = 'views.handler404'

urlpatterns = [
    path("", views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('shop', views.shop, name='shop'),
    path('thankyou', views.thankyou, name='thankyou')
]

