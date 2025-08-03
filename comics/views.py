from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ComicDetails,ComicGenre
# Create your views here.

def home(request):
    genres = ComicGenre.objects.all()[:3]
    genre_books = []
    
    for genre in genres:
        books = genre.comicdetails_set.all()[:4]
        genre_books.append((genre, books))  # List of tuples

    context = {
        'genres_books': genre_books,
        'active_page' :'home'
    }
    return render(request, 'comics/home.html', context)

def genre(response):
      genres = ComicGenre.objects.all()
      books = ComicDetails.objects.all()

      config = {'genres': genres,'books':books}

      return render(response, 'comics/genre.html',config )


def about(response):     
     return render(response,'comics/AboutPage.html',{})

def book(response,name):
    config = {
         'book_name':name
    }
    return render(response,'comics/specificBook.html',config)

def specificGenre(response,GenreName):
     genres = ComicGenre.objects.all()
     selected_genre = ComicGenre.objects.get(gname=GenreName)
     books = selected_genre.comicdetails_set.all()
     config = {
          'genres': genres,'books':books
     }
     return render(response, 'comics/genre.html',config)
