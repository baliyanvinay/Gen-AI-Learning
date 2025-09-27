from mcp.server.fastmcp import FastMCP
from typing import List, Dict

mcp = FastMCP(name="Main Server")


@mcp.tool()
def restart_server(server_config: dict) -> bool:
    """Restart a virtual machine and returns the success status as bool value"""
    print("Connected to the server")
    print("Restart initiated for the server")
    print("Ping status after server restart: %s", bool(True))
    return True


@mcp.tool()
def stop_server(server_id: str) -> bool:
    """Stop a server by its ID and returns the success status as bool value"""
    print(f"Stopping server with ID: {server_id}")
    print("Server stopped successfully")
    return True


@mcp.resource(uri="resource://server/{server_id}/status")
def get_server_status(server_id: str) -> Dict:
    """Get the status of a server by its ID."""
    server_status = {
        "server_id": server_id,
        "status": "running",
        "uptime": "72 hours",
        "load": "moderate",
    }
    return server_status


@mcp.resource(uri="resource://servers/list")
def list_all_servers() -> List[Dict]:
    """List all servers with their statuses."""
    return [
        {"server_id": "srv1", "status": "running"},
        {"server_id": "srv2", "status": "stopped"},
        {"server_id": "srv3", "status": "running"},
    ]


@mcp.prompt(title="Server Maintenance Email")
def server_maintenance_prompt() -> str:
    return f"""
    Write an email draft about the scheduled maintenance of the servers. 
    Use the details below for the email content.
    Subject: Scheduled Server Maintenance Notification
    Signature: IT Support Team
    Server Details: '<list_of_servers>'
    """


@mcp.prompt(title="Get Server Status Structured")
def server_status_structured() -> str:
    return f"""
    Given the server status details below, provide a structured summary.
    Rules: - Use bullet points for each key detail.
           - Highlight any critical issues.
    Example of output:
    - Server ID: '<server_id>'
    - Status: '<status>'
    - Uptime: '<uptime>'
    - Load: '<load>'
    """


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
