from config import *
from pymongo.mongo_client import MongoClient
import asyncio
from pymongo.server_api import ServerApi
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
from chanel import *


uri = "mongodb+srv://akhil:BveFI008IWZlYLPg@ramanan.rx6xwkn.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
