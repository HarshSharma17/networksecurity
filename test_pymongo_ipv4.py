
import os
import socket
from pymongo import MongoClient

uri = os.environ.get("MONGODB_URI")

if not uri:
    raise RuntimeError("MONGODB_URI is not set in this terminal.")

# Diagnostic only: prefer IPv4 when resolving MongoDB node hostnames.
original_getaddrinfo = socket.getaddrinfo

def ipv4_only(host, port, family=0, type=0, proto=0, flags=0):
    if isinstance(host, str) and host.endswith(".mongodb.net"):
        family = socket.AF_INET

    return original_getaddrinfo(
        host, port, family, type, proto, flags
    )

socket.getaddrinfo = ipv4_only

client = MongoClient(uri, serverSelectionTimeoutMS=15000)

try:
    print("Testing PyMongo with IPv4 resolution...")
    print(client.admin.command("ping"))
    print("SUCCESS: PyMongo connected to Atlas!")
except Exception as e:
    print(type(e).__name__)
    print(e)
finally:
    client.close()
    socket.getaddrinfo = original_getaddrinfo
