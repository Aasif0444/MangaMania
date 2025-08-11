from django.contrib import admin
from .models import ComicDetails,ComicGenre,ComidEpisodes

# Register your models here.


admin.site.register(ComicDetails)
admin.site.register(ComicGenre)
admin.site.register(ComidEpisodes)
