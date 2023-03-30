import asyncio
import websockets
import downloader
import config

async def echo(websocket):
    async for message in websocket:
        downloader.send_fic(message, config.email_address, config.password, config.kindle_email)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())