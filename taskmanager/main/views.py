from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about_us.html')


def comment(request):
    return render(request, 'main/comments.html')


def contact(request):
    return render(request, 'main/contacts.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')
