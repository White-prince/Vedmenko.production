from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about-us', views.about, name='about'),
    path('price', views.price, name='price'),
    path('contact', views.get_contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
]
