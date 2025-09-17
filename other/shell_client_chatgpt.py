# football_client.py
import asyncio
from fastmcp import Client

# Point directly at your FastMCP Cloud server's MCP endpoint
client = Client("https://dual-halibut.fastmcp.app/mcp")

async def main():
    async with client:
        # Sanity check that the connection works
        await client.ping()
        print("✅ Connected to dual-halibut")

        # Discover what the server exposes
        tools = await client.list_tools()
        print("\nTools:")
        for t in tools:
            print(f" - {t.name}: {t.description}")

        resources = await client.list_resources()
        print("\nResources:")
        for r in resources:
            print(f" - {r.name}: {r.description}")

        prompts = await client.list_prompts()
        print("\nPrompts:")
        for p in prompts:
            print(f" - {p.name}: {p.description}")

        # Example: call a tool if it's present
        if any(t.name == "echo_tool" for t in tools):
            result = await client.call_tool("echo_tool", {"text": "Hello from FastMCP Client"})
            print("\nResult from echo_tool:", result)
        else:
            print("\nNo echo_tool found on this server.")

if __name__ == "__main__":
    asyncio.run(main())
