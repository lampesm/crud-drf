from rest_framework import generics

from .serializer import MovieSerializer
from .models import Movie


class MovieCreateApi(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
