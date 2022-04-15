from django.urls import path

from .views import MovieCreateApi, MovieReadApi

urlpatterns = [
    path('v1/create', MovieCreateApi.as_view(), name='create'),
    path('v1/read', MovieReadApi.as_view(), name='read'),
]