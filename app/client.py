from channels.consumer import AsyncConsumer

import json
import scrape
from pprint import pprint


class PracticeConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)

        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print("retrive", event, type(event))

        if event['text'] == "1":
            data = scrape.scrape_data()
            pprint(data)
            await self.send({"type": "websocket.send", "text": json.dumps(data)})

    async def websocket_disconnect(self, event):
        print("disconnected", event)
