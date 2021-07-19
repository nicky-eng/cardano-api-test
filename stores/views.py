from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. Heroku is working with Django.")