from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Movie(models.Model):
    name = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    imdb_score = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['imdb_score']
