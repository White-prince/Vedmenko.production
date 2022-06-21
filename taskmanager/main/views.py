from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from taskmanager.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL



def homepage(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about_us.html')


def comment(request):
    return render(request, 'main/comments.html')

#def contact(request):
    #return render(request, 'main/contacts.html')

def get_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']

            recipients = ['alekceev101@gmail.com']

            send_mail(name, message, sender, recipients)

            return HttpResponseRedirect('homepage')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'main/contacts.html', {'form': form})


def portfolio(request):
    return render(request, 'main/portfolio.html')
