from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerViewSet(viewsets.ViewSet):
    
    def list(self, request):
        # /api/player
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def create(self, request):
        # /api/player
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        # /api/player/<int:pk>
        player = Player.objects.get(id=pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # /api/player/<int:pk>
        player = Player.objects.get(id=pk)
        serializer = PlayerSerializer(instance=player, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        # /api/player/<int:pk>
        if(pk == 1):
            return Response(status=status.HTTP_403_FORBIDDEN)
        player = Player.objects.get(id=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)