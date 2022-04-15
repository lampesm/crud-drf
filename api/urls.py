from django.urls import path

from .views import MovieCreateApi, MovieReadApi, MovieUpdateApi

urlpatterns = [
    path('v1/create', MovieCreateApi.as_view(), name='create'),
    path('v1/read', MovieReadApi.as_view(), name='read'),
    path('v1/update/<int:pk>', MovieUpdateApi.as_view(), name='update'),
]