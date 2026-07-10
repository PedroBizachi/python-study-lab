from typing import TypedDict

# TODO: Define a TypedDict named `ServerData`.
# It should have the following required keys and types:
# - hostname: str
# - ip_address: str
# - cpu_cores: int
# - memory_gb: int
# - is_virtual: bool

class ServerData(TypedDict):
    hostname: str
    ip_address: str
    cpu_cores: int
    memory_gb: int
    is_virtual: bool

# TODO: Implement the server class with correct typed __init__ parameters

class Server:
    def __init__(self, hostname: str, ip_address: str, cpu_cores: int, memory_gb: int, is_virtual: bool) -> None:
        self.hostname = hostname
        self.ip_address = ip_address
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
        self.is_virtual = is_virtual

# TODO: Add type hints to the function signature below.
# - The `data` parameter should be of type `ServerData`.
# - The function return value should be of type `Server`.
def create_server_from_data(data: ServerData) -> Server:
    """
    Factory function to create a Server instance from a dictionary.
    """
    # The logic is complete. Your task is to add the type hints.
    return Server(**data)
