from django.http import HttpResponse
from django.shortcuts import render

data = {
    'personal_web':[
    {
        'id':5,
        'title': 'Jaws',
        'year': 1669
    },
    {
        'id':7,
        'title': 'poop',
        'year': 1609
    },
    {
        'id':8,
        'title': 'pee',
        'year': 1069
    }
    ]
}

def personal_web(request):
    return render(request, 'personal_web/index.html', data)


def home(request):
    return HttpResponse("Home page")