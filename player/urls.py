from django.urls import path

from .views import PlayerViewSet, RPSView

urlpatterns = [
    path('players', PlayerViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('players/<int:pk>', PlayerViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
