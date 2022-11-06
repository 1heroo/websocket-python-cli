import sys
import asyncio
import websockets
from getmac import get_mac_address as gma
from websockets.exceptions import ConnectionClosedError


async def ainput(string: str) -> str:
    await asyncio.get_event_loop().run_in_executor(
            None, lambda s=string: sys.stdout.write(s+' '))
    return await asyncio.get_event_loop().run_in_executor(
            None, sys.stdin.readline)


async def test(nickname: str = 'anonymous'):
    async with websockets.connect(f'ws://127.0.0.1:8000/ws/{nickname}') as websocket:
        try:
            await websocket.send(gma() + ' speaker')
            async for message in websocket:
                line = await ainput('enter mesasage: ')
                await websocket.send(line)
        except ConnectionClosedError:
            exit('Enter again with listener client')


if __name__ == '__main__':
    nickname = input('Enter your nickname: ')
    if nickname:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test(nickname=nickname))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
