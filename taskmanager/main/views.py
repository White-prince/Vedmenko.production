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


def contact(request):
    return render(request, 'main/contacts.html')
    if form.is_valid():
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['alekceev101@gmail.com']
        if cc_myself:
            recipients.append(name)

        send_mail(name, message, from_email, recipients)
        return HttpResponseRedirect('/thanks/')


def portfolio(request):
    return render(request, 'main/portfolio.html')
