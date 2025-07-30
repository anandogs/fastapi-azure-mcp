import asyncio
from fastmcp import Client
import httpx

token = "<Enter your token here>"

auth = httpx.Auth()

def bearer_auth(request):
    request.headers["Authorization"] = f"Bearer {token}"
    return request

client = Client(
    "http://localhost:8000/mcp",
    auth=bearer_auth
)

async def main():
    async with client:
        await client.ping()
        tools = await client.list_tools()
        print("Available tools:", tools)

asyncio.run(main())