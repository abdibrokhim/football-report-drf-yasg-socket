from channels.consumer import AsyncConsumer
from app import models, serializers
from asgiref.sync import sync_to_async


@sync_to_async
def _get_data():
    games = models.Game.objects.all()
    serializer = serializers.GameSerializer(games, many=True)
    return serializer.data


@sync_to_async
def _get_datas():
    game = models.Game.objects.all()
    return game


class PracticeConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        await self.send({"type": "websocket.accept"})

        game = await _get_datas()
        print(game)

        data = await _get_data()
        print(data)

        await self.send({"type": "websocket.send", "text": data})

    # async def websocket_receive(self, event):
    #     print("receive", event)
    #
    #     data = await _get_data()
    #     print(data)
    #
    #     sleep(1)
    #
    #     await self.send({"type": "websocket.send", "text": data})

    async def websocket_disconnect(self, event):
        print("disconnected", event)
