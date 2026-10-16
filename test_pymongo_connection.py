
import os
from pymongo import MongoClient

# Set MONGODB_URI in your terminal before running this script.
uri = os.environ.get("MONGODB_URI")

if not uri:
    raise RuntimeError("MONGODB_URI environment variable is not set.")

client = MongoClient(uri, serverSelectionTimeoutMS=15000)

try:
    print("Connecting to MongoDB Atlas...")
    print(client.admin.command("ping"))
    print("MongoDB Atlas connection successful!")
except Exception as e:
    print(type(e).__name__)
    print(e)
finally:
    client.close()
