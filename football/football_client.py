import asyncio
from fastmcp import Client

client = Client("https://ryan-football-server.fastmcp.app/mcp")

async def call_tool():
    async with client:
        result = await client.call_tool("get_counts")
        print(result)

asyncio.run(call_tool())