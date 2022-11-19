#exec(open("async_http_requests.py").read())
import asyncio
import aiohttp
import json

async def main_async():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.publicapis.org/entries', ssl = False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            data = await response.json()
            with open("./content.json", "wt") as fl:
                json.dump(data, fl, indent = 4)

if __name__ == "__main__":
    asyncio.run(main_async())