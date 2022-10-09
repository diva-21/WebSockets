import websockets
import asyncio

async def client_handle():
    url="ws://localhost:7890"
    async with websockets.connect(url) as ws:
        # await ws.send("Hello Groundstation ")
        # direction = await ws.recv()
        # print("The data received from Server" + direction)
        # await ws.send("yes Drone took " + direction)
        # await
        try:

            while 1:
                direction = await ws.recv()
                print("The data received from Server" + direction)
                await ws.send("yes Drone took " + direction)
        except:
            print("Connection closed")

#start running but its controlled by the function which we provide
asyncio.get_event_loop().run_until_complete(client_handle())
