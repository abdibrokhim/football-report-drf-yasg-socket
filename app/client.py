from channels.consumer import AsyncConsumer

import scrape
from app import models, serializers
from asgiref.sync import sync_to_async


# @sync_to_async
# def _get_data():
#     games = models.Game.objects.all()
#     serializer = serializers.GameSerializer(games, many=True)
#     return serializer.data
#
#
# @sync_to_async
# def _get_datas():
#     game = models.Game.objects.all()
#     return game


class PracticeConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        await self.send({"type": "websocket.accept"})

        data = scrape.scrape_data()
        print('client.py data:', data)

        await self.send({"type": "websocket.send", "text": [i.encode('utf-8') for i in data]})

    async def websocket_disconnect(self, event):
        print("disconnected", event)
