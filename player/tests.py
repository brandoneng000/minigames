from typing import OrderedDict
from django.test import TestCase
from player.models import Player
from django.http import HttpRequest
from random import randint
from time import sleep
from collections import OrderedDict

from player.serializers import PlayerSerializer
from player.views import PlayerViewSet

# Create your tests here.
class PlayerTests(TestCase):
    def setUp(self) -> None:
        Player.objects.create(won=5, played=5)
    
    def test_players_count(self):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        self.assertEquals(len(serializer.data), 1)

    def test_player(self):
        player = Player.objects.get(id=1)
        serializer = PlayerSerializer(player)
        self.assertEquals(serializer.data, {'id': 1, 'won': 5, 'loss': 0, 'ties': 0, 'played': 5})

class PlayerViewTests(TestCase):
    
    def test_empty_player_list(self):
        request = HttpRequest()
        response = PlayerViewSet.list(self, request)
        self.assertEquals(response.status_code, 200)

    def test_player_bad_create(self):
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 0, 'ties': 0, 'played': 10}
        response = PlayerViewSet.create(self, request)
        self.assertEquals(response.status_code, 406)

    def test_player_create(self):
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 0, 'ties': 0, 'played': 5}
        response = PlayerViewSet.create(self, request)
        self.assertEquals(response.status_code, 201)

    def test_player_retrieve(self):
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 0, 'ties': 0, 'played': 5}
        createResponse = PlayerViewSet.create(self, request)
        request = HttpRequest()
        response = PlayerViewSet.retrieve(self, request, createResponse.data['id']).data
        self.assertEquals(response['won'], 5)
        self.assertEquals(response['loss'], 0)
        self.assertEquals(response['ties'], 0)
        self.assertEquals(response['played'], 5)

    def test_player_bad_update(self):
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 0, 'ties': 0, 'played': 5}
        createResponse = PlayerViewSet.create(self, request)
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 0, 'ties': 0, 'played': 15}
        response = PlayerViewSet.update(self, request, createResponse.data['id'])
        self.assertEquals(response.status_code, 304)

    def test_player_good_update(self):
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 0, 'ties': 0, 'played': 5}
        createResponse = PlayerViewSet.create(self, request)
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 5, 'ties': 5, 'played': 15}
        response = PlayerViewSet.update(self, request, createResponse.data['id'])
        self.assertEquals(response.status_code, 202)
        self.assertEquals(response.data['won'], 5)
        self.assertEquals(response.data['loss'], 5)
        self.assertEquals(response.data['ties'], 5)
        self.assertEquals(response.data['played'], 15)

    def test_fail_destroy(self):
        request = HttpRequest()
        response = PlayerViewSet.destroy(self, request, 1)
        self.assertEquals(response.status_code, 403)

    def test_pass_destroy(self):
        request = HttpRequest()
        request.data = {'won': 5, 'loss': 0, 'ties': 0, 'played': 5}
        createResponse = PlayerViewSet.create(self, request)
        request = HttpRequest()
        response = PlayerViewSet.destroy(self, request, createResponse.data['id'])
        self.assertEquals(response.status_code, 204)

    def test_large_list_create(self):
        requestList = []
        statusList = []
        request = HttpRequest()
        request.data = {'won': 0, 'loss': 0, 'ties': 0, 'played': 0}
        createResponse = PlayerViewSet.create(self, request)
        requestList.append(OrderedDict(createResponse.data))
        statusList.append(createResponse.status_code)
        sleep(0.01)
        for index in range(10):
            rand = randint(0, 2)
            if rand == 0:
                request.data['won'] += 5
            elif rand == 1:
                request.data['loss'] += 5
            elif rand == 2:
                request.data['ties'] += 5
            request.data['played'] += 5
            createResponse = PlayerViewSet.create(self, request)
            requestList.append(OrderedDict(createResponse.data))
            statusList.append(createResponse.status_code)
            sleep(0.01)

        request = HttpRequest()
        response = PlayerViewSet.list(self, request)
        for status in statusList:
            self.assertEquals(status, 201)
        self.assertListEqual(response.data, requestList)