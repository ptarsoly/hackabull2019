

import asyncio
import websockets

ip_address = '10.245.16.6'

async def hello(websocket, path):
  pait = await websocket.recv()
  print("Patient : {}",format(pait))

  greeting = input()

  await websocket.send(greeting)
  print(f"> {greeting}")

start_server = websockets.serve(hello, ip_address, 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()