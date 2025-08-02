from django.contrib import admin
from .models import ComicDetails,ComicGenre

# Register your models here.


admin.site.register(ComicDetails)
admin.site.register(ComicGenre)

