import websockets
import asyncio
import time
PORT=7890
l=["left","right","top","down"]
print("Server started on " +str(PORT))
#here arg websocket is an instance of the websocket of the client
async def server_handle(websocket):
    print("A client just connected")
    for i in l:
        await websocket.send(i)
        msg = await websocket.recv()
        print("client: " + msg)






#starting the server async way
start_server=websockets.serve(server_handle,"localhost",PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()






