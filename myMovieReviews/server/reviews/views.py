from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
# Create your views here.

def index(request):
    return HttpResponse("Hello,world. reviews인덱스")

def detail(request, movie_id):
    template = loader.get_template('reviews/detail.html')
    context = {
        'movie_id': movie_id,
    }
    return HttpResponse(template.render(context, request))

def write(request,):
    response = "writepage"
    return HttpResponse(response)

def vote(request, movie_id):
    return HttpResponse("You're voting on question %s." % movie_id)

def index(request):
    latest_movie_list = Movie.objects.order_by('-nameMv')[:5]
    output = ', '.join([Movie for m in latest_movie_list])
    return HttpResponse(output)

def index(request,):
    latest_movie_list = Movie.objects.order_by('-nameMv')[:5]
    template = loader.get_template('reviews/index.html')
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return HttpResponse(template.render(context, request))

