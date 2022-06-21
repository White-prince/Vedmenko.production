from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('about-us', views.about, name='about'),
    path('comments', views.comment, name='comment'),
    path('contact', views.get_contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
]
