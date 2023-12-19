from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    return render(request, 'school_app/index.html')


def courses(request):
    data = {
        'obj': [
            {   'image': 'course-01.jpg',
                'header': 'Курс для начинающих',
                'description': 'descript',
                'author_image': "courses/author-02.png",
                'is_free': True,
            },
            {
                'image': 'course-02',
                'header': 'Курс для опытных',
                'description': 'descript',
                'author_image': 'products/author-02.png',
                'is_free': False,
            },
            {
                'image': 'course-03',
                'header': 'Курс для профессионалов',
                'description': 'descript',
                'author_image': 'products/author-03.jpg',
                'is_free': False,
            },
        ]
    }
    return render(request, 'school_app/courses.html', context = data)


def presentation(request):
    return render(request, 'school_app/presentation.html')

def contact(request):
    return render(request, 'school_app/contact.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('404')
