from django.urls import path

from .views import MovieCreateApi

urlpatterns = [
    path('v1/create', MovieCreateApi.as_view(), name='create'),
]