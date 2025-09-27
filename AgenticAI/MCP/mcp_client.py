from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

connections = {
    "vm_test_server": {
        "url": "http://localhost:8000/mcp",
        "transport": "streamable_http",
    }
}

client = MultiServerMCPClient(connections=connections)
async def main():
    available_tools = await client.get_tools()
    print("Available Tools:", available_tools)
    available_resources = await client.get_resources(server_name="vm_test_server")
    print("Available Resources:", available_resources)
    available_prompts = await client.get_prompt(server_name="vm_test_server", prompt_name="server_status_structured")
    print("Available Prompts:", available_prompts)
asyncio.run(main())
