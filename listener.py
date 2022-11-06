import asyncio
import websockets
from getmac import get_mac_address as gma


async def test(nickname: str = 'anonymous'):
    async with websockets.connect(f'ws://127.0.0.1:8000/ws/{nickname}') as websocket:
        await websocket.send(gma())
        async for message in websocket:
            print(message)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
