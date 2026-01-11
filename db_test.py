
# from pymongo import MongoClient
# #from collections.abc import MutableMapping

# uri = "mongodb+srv://akileshramkumar_db_user:Vell!0905@cluster0.p8htxvf.mongodb.net/?appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from pymongo import MongoClient
import os

uri = "mongodb+srv://akileshramkumar_db_user:Vell!0905@cluster1.tci8mbd.mongodb.net/?appName=Cluster1"

client = MongoClient(uri, serverSelectionTimeoutMS=5000)

client.admin.command("ping")
print("MongoDB connected successfully")