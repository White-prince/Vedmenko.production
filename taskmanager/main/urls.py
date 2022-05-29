from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about-us', views.about, name='about'),
    path('comments', views.comment, name='comment'),
    path('contacts', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
]
