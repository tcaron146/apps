from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import PersonalWeb

def personal_web_view(request):
    data = PersonalWeb.objects.all()
    return render(request, 'personal_web/index.html', {'data': data})


def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = PersonalWeb.objects.get(pk=id)
    return render(request, 'personal_web/beer.html', {'personal_web': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = PersonalWeb(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/personal_web')

    return render(request, 'personal_web/reviews.html')