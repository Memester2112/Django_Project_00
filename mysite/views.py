from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2> Hello, world. From mysite folder </h2>")