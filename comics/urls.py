from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='homepage'),
    path('genre/',views.genre,name='genrapage'),
    path('about/',views.about,name='aboutpage'),
    path('book/<str:name>/',views.book,name='bookpage'),
]