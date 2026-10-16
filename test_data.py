
import os
import ssl
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")

print("Python OpenSSL:", ssl.OPENSSL_VERSION)

client = None

try:
    client = MongoClient(
        uri,
        tls=True,
        serverSelectionTimeoutMS=15000,
    )

    print(client.admin.command("ping"))
    print("Connected successfully!")

except Exception as e:
    print(type(e).__name__)
    print(str(e))

finally:
    if client is not None:
        client.close()
