from django.contrib import admin

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'director',
        'release_date',
        'imdb_score',
        'author',
        'content',
        'publish',
        'created',
        'updated',
        'status',
    )
    list_filter = ('status',)
    search_fields = ('name', 'director', 'content')


admin.site.register(Movie, MovieAdmin)
