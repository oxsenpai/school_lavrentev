from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    return render(request, 'school_app/index.html')


def courses(request):
    return render(request, 'school_app/courses.html')


def presentation(request):
    return render(request, 'school_app/presentation.html')

def contact(request):
    return render(request, 'school_app/contact.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('404')
